from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'email', 'password', 'password_confirm'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                "Пароли не совпадают"
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """Сериализатор для входа пользователя"""
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )

            if not user:
                raise serializers.ValidationError(
                    'Неверный email или пароль'
                )

            if not user.is_active:
                raise serializers.ValidationError(
                    'Аккаунт пользователя деактивирован'
                )

            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError(
                'Необходимо указать email и пароль'
            )


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для профиля пользователя"""
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 
            'birthday', 'occupation', 'sex', 'role',
            'date_joined', 'last_login'
        ]
        read_only_fields = ['id', 'email', 'role', 'date_joined', 'last_login']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления профиля пользователя"""
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'birthday', 
            'occupation', 'sex'
        ]


class ChangePasswordSerializer(serializers.Serializer):
    """Сериализатор для смены пароля"""
    old_password = serializers.CharField(
        style={'input_type': 'password'}
    )
    new_password = serializers.CharField(
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    new_password_confirm = serializers.CharField(
        style={'input_type': 'password'}
    )

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Неверный старый пароль')
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError(
                'Новые пароли не совпадают'
            )
        return attrs

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user