import asyncio
import json
from uuid import uuid4

from rest_framework import status, generics, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

from temporalio.client import Client
from temporalio.service import RPCError, RPCStatusCode

from core.decorators import (
    cache_api_response, cache_course_data, invalidate_course_cache,
    api_rate_limit, generation_rate_limit
)
from core.redis_utils import CourseCache, GenerationCache

from .models import Course, Module, Chapter, CourseCategory
from .serializers import (
    CourseSerializer, CourseListSerializer, CourseDetailSerializer,
    ModuleSerializer, ChapterSerializer, CourseCategorySerializer,
    CourseGenerationSerializer
)
# Temporal workflow will be imported dynamically to avoid import errors
# from aikademiya.temporal_app.workflows import GenerateCourseWorkflow


class CourseCategoryListView(generics.ListCreateAPIView):
    """
    Список категорий курсов
    """
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="Список категорий курсов",
        description="Получение списка всех категорий курсов"
    )
    @cache_api_response(timeout=1800)  # Кешируем на 30 минут
    @api_rate_limit
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Создать категорию",
        description="Создание новой категории курсов (только для админов)"
    )
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({
                'error': 'Только администраторы могут создавать категории'
            }, status=status.HTTP_403_FORBIDDEN)
        return super().post(request, *args, **kwargs)


class CourseListCreateView(generics.ListCreateAPIView):
    """
    Список курсов и создание новых курсов
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['level', 'language', 'category', 'is_public']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Course.objects.select_related('created_by', 'category').prefetch_related('modules')
        
        # Если пользователь не авторизован или не владелец, показываем только публичные курсы
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_public=True)
        elif self.request.query_params.get('my_courses') == 'true':
            # Показать только курсы пользователя
            queryset = queryset.filter(created_by=self.request.user)
        elif not self.request.user.is_staff:
            # Для обычных пользователей показываем публичные курсы + свои курсы
            queryset = queryset.filter(
                Q(is_public=True) | Q(created_by=self.request.user)
            )
        
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CourseListSerializer
        return CourseSerializer

    @extend_schema(
        summary="Список курсов",
        description="Получение списка курсов с фильтрацией и поиском",
        parameters=[
            OpenApiParameter('level', str, description='Фильтр по уровню сложности'),
            OpenApiParameter('language', str, description='Фильтр по языку'),
            OpenApiParameter('category', int, description='Фильтр по категории'),
            OpenApiParameter('search', str, description='Поиск по названию и описанию'),
            OpenApiParameter('my_courses', bool, description='Показать только мои курсы'),
        ]
    )
    @cache_api_response(timeout=600)  # Кешируем на 10 минут
    @api_rate_limit
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Создать курс",
        description="Создание нового курса",
        request=CourseSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детальная информация о курсе, обновление и удаление
    """
    queryset = Course.objects.select_related('created_by', 'category').prefetch_related(
        'modules__chapters'
    )
    serializer_class = CourseDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def get_object(self):
        obj = super().get_object()
        
        # Проверяем права доступа
        if self.request.method == 'GET':
            if not obj.is_public and obj.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет доступа к этому курсу")
        else:
            # Для изменения/удаления только владелец или админ
            if obj.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет прав на изменение этого курса")
        
        return obj

    @extend_schema(
        summary="Детали курса",
        description="Получение подробной информации о курсе включая модули и главы"
    )
    @cache_course_data(timeout=1800)  # Кешируем на 30 минут
    @api_rate_limit
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить курс",
        description="Обновление информации о курсе (только владелец или админ)"
    )
    @invalidate_course_cache
    @api_rate_limit
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить курс",
        description="Удаление курса (только владелец или админ)"
    )
    @invalidate_course_cache
    @api_rate_limit
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детальная информация о модуле
    """
    queryset = Module.objects.select_related('course').prefetch_related('chapters')
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        
        # Проверяем права доступа через курс
        if self.request.method == 'GET':
            if not obj.course.is_public and obj.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет доступа к этому модулю")
        else:
            if obj.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет прав на изменение этого модуля")
        
        return obj


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детальная информация о главе
    """
    queryset = Chapter.objects.select_related('module__course')
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        
        # Проверяем права доступа через курс
        if self.request.method == 'GET':
            if not obj.module.course.is_public and obj.module.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет доступа к этой главе")
        else:
            if obj.module.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет прав на изменение этой главы")
        
        return obj


# Функции для работы с Temporal workflow (генерация курсов)
async def _start_workflow(topic: str) -> str:
    try:
        from aikademiya.temporal_app.workflows import GenerateCourseWorkflow
    except ImportError:
        raise Exception("Temporal workflow не настроен")
    
    client = await Client.connect("temporal:7233")
    handle = await client.start_workflow(
        GenerateCourseWorkflow.run,
        topic,
        id=f"course-{uuid4()}",
        task_queue="course-task-queue",
    )
    return handle.id


async def _signal_workflow(workflow_id: str, signal: str, payload) -> None:
    client = await Client.connect("temporal:7233")
    handle = client.get_workflow_handle(workflow_id)
    await handle.signal(signal, payload)


async def _workflow_status(workflow_id: str):
    client = await Client.connect("temporal:7233")
    handle = client.get_workflow_handle(workflow_id)
    try:
        info = await handle.query("get_state")
    except RPCError as err:
        if err.status == RPCStatusCode.DEADLINE_EXCEEDED:
            return {"error": "timeout"}
        raise

    if info.get("status") == "completed":
        result = await handle.result()
        info["result"] = result
    return info


class CourseGenerationView(APIView):
    """
    Генерация курса с помощью ИИ
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Запустить генерацию курса",
        description="Запуск процесса генерации курса с помощью ИИ",
        request=CourseGenerationSerializer,
        responses={
            200: OpenApiResponse(description="Генерация запущена"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    @generation_rate_limit  # Ограничение на генерацию
    def post(self, request):
        serializer = CourseGenerationSerializer(data=request.data)
        if serializer.is_valid():
            topic = serializer.validated_data['topic']
            try:
                workflow_id = asyncio.run(_start_workflow(topic))
                
                # Сохраняем статус генерации в кеш
                GenerationCache.set_generation_status(workflow_id, {
                    'status': 'started',
                    'topic': topic,
                    'user_id': request.user.id,
                    'created_at': json.dumps({'timestamp': 'now'})  # Заменим на реальное время
                })
                
                return Response({
                    'workflow_id': workflow_id,
                    'message': 'Генерация курса запущена',
                    'topic': topic
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    'error': f'Ошибка запуска генерации: {str(e)}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="Статус генерации курса",
    description="Получение статуса процесса генерации курса",
    responses={
        200: OpenApiResponse(description="Статус получен"),
        504: OpenApiResponse(description="Таймаут"),
        404: OpenApiResponse(description="Workflow не найден")
    }
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@api_rate_limit
def course_generation_status(request, workflow_id: str):
    """
    Получение статуса генерации курса
    """
    # Проверяем кеш сначала
    cached_status = GenerationCache.get_generation_status(workflow_id)
    if cached_status:
        return Response(cached_status, status=status.HTTP_200_OK)
    
    try:
        info = asyncio.run(_workflow_status(workflow_id))
        if isinstance(info, dict) and info.get("error") == "timeout":
            return Response(info, status=status.HTTP_504_GATEWAY_TIMEOUT)
        
        # Сохраняем статус в кеш
        GenerationCache.set_generation_status(workflow_id, info)
        
        return Response(info, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': f'Ошибка получения статуса: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    summary="Подтвердить генерацию курса",
    description="Подтверждение сгенерированного курса",
    responses={
        200: OpenApiResponse(description="Курс подтвержден"),
        400: OpenApiResponse(description="Ошибка подтверждения")
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@api_rate_limit
def confirm_course_generation(request, workflow_id: str):
    """
    Подтверждение сгенерированного курса
    """
    try:
        asyncio.run(_signal_workflow(workflow_id, "confirm", True))
        
        # Обновляем статус в кеше
        GenerationCache.set_generation_status(workflow_id, {
            'status': 'confirmed',
            'user_id': request.user.id
        })
        
        return Response({
            'message': 'Курс подтвержден'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': f'Ошибка подтверждения: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    summary="Сгенерировать следующую главу",
    description="Запуск генерации следующей главы курса",
    responses={
        200: OpenApiResponse(description="Генерация следующей главы запущена"),
        400: OpenApiResponse(description="Ошибка запуска генерации")
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@generation_rate_limit
def generate_next_chapter(request, workflow_id: str):
    """
    Генерация следующей главы курса
    """
    try:
        asyncio.run(_signal_workflow(workflow_id, "next_chapter", None))
        return Response({
            'message': 'Генерация следующей главы запущена'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': f'Ошибка генерации: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)