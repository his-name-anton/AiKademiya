"""
Декораторы для кеширования и ограничения скорости запросов.
"""

import hashlib
import json
from functools import wraps
from typing import Any, Callable, Optional

from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django_ratelimit.decorators import ratelimit
from rest_framework.response import Response
from rest_framework import status

from .redis_utils import RedisCache, APICache


def cache_api_response(timeout: int = 300, vary_on: Optional[list] = None):
    """
    Декоратор для кеширования API ответов.
    
    Args:
        timeout: Время жизни кеша в секундах
        vary_on: Список заголовков, от которых зависит кеширование
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Формируем ключ кеша на основе URL, параметров и заголовков
            cache_key_data = {
                'path': request.path,
                'method': request.method,
                'params': dict(request.GET.items()),
                'user_id': request.user.id if request.user.is_authenticated else None,
            }
            
            # Добавляем указанные заголовки в ключ кеша
            if vary_on:
                headers = {}
                for header in vary_on:
                    headers[header] = request.META.get(f'HTTP_{header.upper().replace("-", "_")}', '')
                cache_key_data['headers'] = headers
            
            # Создаем хеш ключа
            cache_key_str = json.dumps(cache_key_data, sort_keys=True)
            cache_key = f"api_response:{hashlib.md5(cache_key_str.encode()).hexdigest()}"
            
            # Пытаемся получить из кеша
            cached_response = RedisCache.get(cache_key)
            if cached_response is not None:
                return Response(cached_response)
            
            # Выполняем функцию
            response = func(request, *args, **kwargs)
            
            # Кешируем только успешные ответы
            if hasattr(response, 'status_code') and 200 <= response.status_code < 300:
                if hasattr(response, 'data'):
                    RedisCache.set(cache_key, response.data, timeout)
            
            return response
        return wrapper
    return decorator


def cache_course_data(timeout: int = 1800):
    """
    Декоратор для кеширования данных курсов на 30 минут.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Извлекаем course_id из параметров
            course_id = kwargs.get('course_id') or kwargs.get('pk')
            if not course_id:
                return func(request, *args, **kwargs)
            
            cache_key = f"course_data:{course_id}:{request.method}:{request.path}"
            
            # Проверяем кеш
            cached_data = RedisCache.get(cache_key)
            if cached_data is not None:
                return Response(cached_data)
            
            # Выполняем функцию
            response = func(request, *args, **kwargs)
            
            # Кешируем только GET запросы с успешными ответами
            if request.method == 'GET' and hasattr(response, 'status_code') and response.status_code == 200:
                if hasattr(response, 'data'):
                    RedisCache.set(cache_key, response.data, timeout)
            
            return response
        return wrapper
    return decorator


def invalidate_course_cache(func: Callable) -> Callable:
    """
    Декоратор для очистки кеша курса при изменении данных.
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # Выполняем функцию
        response = func(request, *args, **kwargs)
        
        # Если операция успешна, очищаем кеш
        if hasattr(response, 'status_code') and 200 <= response.status_code < 300:
            course_id = kwargs.get('course_id') or kwargs.get('pk')
            if course_id:
                # Очищаем кеш курса
                RedisCache.clear_pattern(f"course:{course_id}*")
                RedisCache.clear_pattern(f"course_data:{course_id}*")
        
        return response
    return wrapper


def cache_user_data(timeout: int = 900):
    """
    Декоратор для кеширования пользовательских данных на 15 минут.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return func(request, *args, **kwargs)
            
            user_id = request.user.id
            cache_key = f"user_data:{user_id}:{request.method}:{request.path}"
            
            # Проверяем кеш
            cached_data = RedisCache.get(cache_key)
            if cached_data is not None:
                return Response(cached_data)
            
            # Выполняем функцию
            response = func(request, *args, **kwargs)
            
            # Кешируем только GET запросы с успешными ответами
            if request.method == 'GET' and hasattr(response, 'status_code') and response.status_code == 200:
                if hasattr(response, 'data'):
                    RedisCache.set(cache_key, response.data, timeout)
            
            return response
        return wrapper
    return decorator


def invalidate_user_cache(func: Callable) -> Callable:
    """
    Декоратор для очистки кеша пользователя при изменении данных.
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # Выполняем функцию
        response = func(request, *args, **kwargs)
        
        # Если операция успешна, очищаем кеш пользователя
        if hasattr(response, 'status_code') and 200 <= response.status_code < 300:
            if request.user.is_authenticated:
                user_id = request.user.id
                RedisCache.clear_pattern(f"user:{user_id}*")
                RedisCache.clear_pattern(f"user_data:{user_id}*")
        
        return response
    return wrapper


# Rate limiting декораторы
api_rate_limit = ratelimit(key='ip', rate='100/h', method='ALL', block=True)
api_rate_limit_strict = ratelimit(key='ip', rate='20/h', method='ALL', block=True)
user_rate_limit = ratelimit(key='user', rate='1000/h', method='ALL', block=True)
generation_rate_limit = ratelimit(key='user', rate='10/h', method='POST', block=True)


def cached_property_redis(timeout: int = 300):
    """
    Декоратор для кеширования свойств модели в Redis.
    """
    def decorator(func: Callable) -> property:
        @wraps(func)
        def wrapper(self):
            cache_key = f"model_property:{self.__class__.__name__}:{self.pk}:{func.__name__}"
            
            cached_value = RedisCache.get(cache_key)
            if cached_value is not None:
                return cached_value
            
            value = func(self)
            RedisCache.set(cache_key, value, timeout)
            return value
        
        return property(wrapper)
    return decorator


def cache_generation_result(timeout: int = 7200):
    """
    Декоратор для кеширования результатов генерации курсов на 2 часа.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем ключ на основе параметров генерации
            cache_key_data = {
                'function': func.__name__,
                'args': str(args),
                'kwargs': str(sorted(kwargs.items()))
            }
            cache_key_str = json.dumps(cache_key_data, sort_keys=True)
            cache_key = f"generation:{hashlib.md5(cache_key_str.encode()).hexdigest()}"
            
            # Проверяем кеш
            cached_result = RedisCache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Выполняем функцию
            result = func(*args, **kwargs)
            
            # Кешируем результат
            RedisCache.set(cache_key, result, timeout)
            
            return result
        return wrapper
    return decorator