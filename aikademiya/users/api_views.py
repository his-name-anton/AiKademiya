from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from drf_spectacular.utils import extend_schema, OpenApiResponse

from core.decorators import (
    cache_user_data, invalidate_user_cache, api_rate_limit, api_rate_limit_strict
)
from core.redis_utils import UserCache

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    """
    Регистрация нового пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Регистрация пользователя",
        description="Создание нового аккаунта пользователя",
        responses={
            201: OpenApiResponse(description="Пользователь успешно зарегистрирован"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    @api_rate_limit_strict  # Ограниченный лимит для регистрации
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Создаем JWT токены
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'success': True,
                'message': 'Пользователь успешно зарегистрирован',
                'data': {
                    'user': UserProfileSerializer(user).data,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    Аутентификация пользователя
    """
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Вход в систему",
        description="Аутентификация пользователя по email и паролю",
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(description="Успешная аутентификация"),
            400: OpenApiResponse(description="Неверные учетные данные")
        }
    )
    @api_rate_limit_strict  # Ограниченный лимит для входа
    def post(self, request):
        serializer = UserLoginSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Создаем JWT токены
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'success': True,
                'message': 'Успешная аутентификация',
                'data': {
                    'user': UserProfileSerializer(user).data,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    Выход из системы
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Выход из системы",
        description="Добавление токена в черный список",
        responses={
            200: OpenApiResponse(description="Успешный выход"),
            400: OpenApiResponse(description="Неверный токен")
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({
                'message': 'Успешный выход из системы'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Неверный токен'
            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Просмотр и обновление профиля пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserProfileSerializer
        return UserUpdateSerializer

    @extend_schema(
        summary="Получить профиль пользователя",
        description="Получение информации о текущем пользователе",
        responses={
            200: UserProfileSerializer,
            401: OpenApiResponse(description="Не авторизован")
        }
    )
    @cache_user_data(timeout=900)  # Кешируем профиль на 15 минут
    @api_rate_limit
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить профиль пользователя",
        description="Обновление информации о текущем пользователе",
        request=UserUpdateSerializer,
        responses={
            200: UserProfileSerializer,
            400: OpenApiResponse(description="Ошибки валидации"),
            401: OpenApiResponse(description="Не авторизован")
        }
    )
    @invalidate_user_cache  # Очищаем кеш при обновлении
    @api_rate_limit
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class ChangePasswordView(APIView):
    """
    Смена пароля пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Сменить пароль",
        description="Смена пароля текущего пользователя",
        request=ChangePasswordSerializer,
        responses={
            200: OpenApiResponse(description="Пароль успешно изменен"),
            400: OpenApiResponse(description="Ошибки валидации"),
            401: OpenApiResponse(description="Не авторизован")
        }
    )
    @api_rate_limit_strict  # Ограниченный лимит для смены пароля
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            serializer.save()
            
            # Очищаем кеш пользователя после смены пароля
            UserCache.clear_user_cache(request.user.id)
            
            return Response({
                'message': 'Пароль успешно изменен'
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="Проверка токена",
    description="Проверка валидности JWT токена",
    responses={
        200: OpenApiResponse(description="Токен валидный"),
        401: OpenApiResponse(description="Токен невалидный")
    }
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@cache_user_data(timeout=300)  # Кешируем проверку токена на 5 минут
@api_rate_limit
def verify_token(request):
    """
    Проверка валидности JWT токена
    """
    return Response({
        'message': 'Токен валидный',
        'user': UserProfileSerializer(request.user).data
    }, status=status.HTTP_200_OK)