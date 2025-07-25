"""
Middleware для мониторинга производительности и работы с кешем.
"""

import time
import logging
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from core.redis_utils import RedisCache

logger = logging.getLogger(__name__)


class CacheStatsMiddleware(MiddlewareMixin):
    """
    Middleware для сбора статистики по использованию кеша.
    """
    
    def process_request(self, request):
        """Запоминаем время начала обработки запроса."""
        request._cache_start_time = time.time()
        request._cache_hits = 0
        request._cache_misses = 0
        return None
    
    def process_response(self, request, response):
        """Логируем статистику кеша для запроса."""
        if hasattr(request, '_cache_start_time'):
            duration = time.time() - request._cache_start_time
            
            # Добавляем заголовки с информацией о производительности
            if hasattr(request, '_cache_hits'):
                response['X-Cache-Hits'] = str(request._cache_hits)
            if hasattr(request, '_cache_misses'):
                response['X-Cache-Misses'] = str(request._cache_misses)
            response['X-Response-Time'] = f"{duration:.3f}s"
            
            # Логируем медленные запросы
            if duration > 1.0:  # Запросы дольше 1 секунды
                logger.warning(
                    f"Медленный запрос: {request.method} {request.path} "
                    f"({duration:.3f}s)"
                )
        
        return response


class RedisHealthCheckMiddleware(MiddlewareMixin):
    """
    Middleware для проверки состояния Redis.
    """
    
    def process_request(self, request):
        """Проверяем доступность Redis для критических эндпоинтов."""
        # Проверяем только для API эндпоинтов
        if request.path.startswith('/api/'):
            try:
                # Простая проверка доступности Redis
                cache.get('_health_check', default='ok')
            except Exception as e:
                logger.error(f"Redis недоступен: {e}")
                # Redis недоступен, но не блокируем запрос
                # Приложение должно продолжать работать
        
        return None


class CacheHeadersMiddleware(MiddlewareMixin):
    """
    Middleware для добавления заголовков кеширования.
    """
    
    def process_response(self, request, response):
        """Добавляем заголовки кеширования для статических API ответов."""
        # Добавляем заголовки только для GET запросов к API
        if (request.method == 'GET' and 
            request.path.startswith('/api/') and 
            response.status_code == 200):
            
            # Определяем время кеширования в зависимости от эндпоинта
            if 'categories' in request.path:
                # Категории меняются редко
                max_age = 1800  # 30 минут
            elif 'courses' in request.path and 'my_courses' not in request.GET:
                # Публичные курсы
                max_age = 600   # 10 минут
            elif 'profile' in request.path:
                # Профили пользователей
                max_age = 300   # 5 минут
            else:
                max_age = 60    # 1 минута по умолчанию
            
            response['Cache-Control'] = f'public, max-age={max_age}'
            response['Vary'] = 'Accept, Authorization'
        
        return response