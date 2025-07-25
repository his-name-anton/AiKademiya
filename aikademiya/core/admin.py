"""
Админ панель для мониторинга Redis кеша.
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from .redis_utils import RedisCache


@method_decorator(staff_member_required, name='dispatch')
class RedisAdminView:
    """Представление для мониторинга Redis в админке."""
    
    def redis_stats_view(self, request):
        """Страница статистики Redis."""
        try:
            from django_redis import get_redis_connection
            redis_conn = get_redis_connection("default")
            info = redis_conn.info()
            
            context = {
                'title': 'Статистика Redis',
                'redis_info': info,
                'has_permission': True
            }
            return render(request, 'admin/redis_stats.html', context)
        except Exception as e:
            context = {
                'title': 'Статистика Redis',
                'error': str(e),
                'has_permission': True
            }
            return render(request, 'admin/redis_stats.html', context)
    
    def clear_cache_view(self, request):
        """API для очистки кеша."""
        if request.method == 'POST':
            pattern = request.POST.get('pattern')
            clear_all = request.POST.get('clear_all') == 'true'
            
            try:
                if clear_all:
                    cache.clear()
                    message = "Весь кеш очищен"
                elif pattern:
                    RedisCache.clear_pattern(pattern)
                    message = f"Кеш по паттерну '{pattern}' очищен"
                else:
                    return JsonResponse({'error': 'Не указан паттерн или флаг clear_all'})
                
                return JsonResponse({'success': True, 'message': message})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        
        return JsonResponse({'error': 'Только POST запросы'})


# Создаем экземпляр для использования в URL
redis_admin = RedisAdminView()


# Регистрируем кастомные URL в админке
class RedisAdminConfig:
    """Конфигурация для добавления Redis админки."""
    
    @staticmethod
    def get_urls():
        """Возвращает дополнительные URL для админки."""
        return [
            path('redis-stats/', redis_admin.redis_stats_view, name='redis_stats'),
            path('redis-clear/', redis_admin.clear_cache_view, name='redis_clear'),
        ]


# Добавляем URL в основной админ сайт
from django.contrib.admin import site
original_get_urls = site.get_urls

def custom_get_urls():
    """Переопределяем метод get_urls для добавления наших URL."""
    urls = original_get_urls()
    custom_urls = RedisAdminConfig.get_urls()
    return custom_urls + urls

site.get_urls = custom_get_urls
