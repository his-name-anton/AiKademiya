"""
Утилиты для работы с Redis кешем.
Предоставляет удобные методы для кеширования данных курсов, пользователей и API ответов.
"""

import json
import logging
from typing import Any, Optional, Dict, List
from django.core.cache import cache
from django.conf import settings
from django.db import models

logger = logging.getLogger(__name__)


class RedisCache:
    """Класс для работы с Redis кешем."""
    
    # Время жизни кеша по умолчанию (в секундах)
    DEFAULT_TIMEOUT = 300  # 5 минут
    
    # Префиксы для разных типов данных
    COURSE_PREFIX = "course:"
    USER_PREFIX = "user:"
    API_PREFIX = "api:"
    STATS_PREFIX = "stats:"
    GENERATION_PREFIX = "generation:"
    
    @classmethod
    def set(cls, key: str, value: Any, timeout: Optional[int] = None) -> bool:
        """
        Сохранить значение в кеш.
        
        Args:
            key: Ключ для сохранения
            value: Значение для сохранения
            timeout: Время жизни в секундах (по умолчанию DEFAULT_TIMEOUT)
        
        Returns:
            bool: True если успешно сохранено
        """
        try:
            if timeout is None:
                timeout = cls.DEFAULT_TIMEOUT
            
            # Если это Django модель, конвертируем в dict
            if isinstance(value, models.Model):
                value = cls._model_to_dict(value)
            
            cache.set(key, value, timeout)
            logger.debug(f"Кеш установлен: {key}")
            return True
        except Exception as e:
            logger.error(f"Ошибка установки кеша {key}: {e}")
            return False
    
    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """
        Получить значение из кеша.
        
        Args:
            key: Ключ для получения
            default: Значение по умолчанию если ключ не найден
        
        Returns:
            Значение из кеша или default
        """
        try:
            value = cache.get(key, default)
            if value != default:
                logger.debug(f"Кеш найден: {key}")
            return value
        except Exception as e:
            logger.error(f"Ошибка получения кеша {key}: {e}")
            return default
    
    @classmethod
    def delete(cls, key: str) -> bool:
        """
        Удалить значение из кеша.
        
        Args:
            key: Ключ для удаления
        
        Returns:
            bool: True если успешно удалено
        """
        try:
            cache.delete(key)
            logger.debug(f"Кеш удален: {key}")
            return True
        except Exception as e:
            logger.error(f"Ошибка удаления кеша {key}: {e}")
            return False
    
    @classmethod
    def clear_pattern(cls, pattern: str) -> bool:
        """
        Удалить все ключи по паттерну.
        
        Args:
            pattern: Паттерн ключей для удаления (например, "course:*")
        
        Returns:
            bool: True если успешно удалено
        """
        try:
            from django_redis import get_redis_connection
            redis_conn = get_redis_connection("default")
            
            # Получаем ключи с префиксом
            full_pattern = f"{settings.CACHES['default']['KEY_PREFIX']}:{pattern}"
            keys = redis_conn.keys(full_pattern)
            
            if keys:
                redis_conn.delete(*keys)
                logger.debug(f"Удалено {len(keys)} ключей по паттерну: {pattern}")
            
            return True
        except Exception as e:
            logger.error(f"Ошибка удаления по паттерну {pattern}: {e}")
            return False
    
    @classmethod
    def _model_to_dict(cls, instance: models.Model) -> Dict:
        """Конвертировать Django модель в словарь для кеширования."""
        data = {}
        for field in instance._meta.fields:
            value = getattr(instance, field.name)
            # Обработка специальных типов
            if hasattr(value, 'isoformat'):  # datetime объекты
                data[field.name] = value.isoformat()
            elif hasattr(value, 'pk'):  # ForeignKey объекты
                data[field.name] = value.pk
            else:
                data[field.name] = value
        return data


class CourseCache:
    """Специализированный класс для кеширования данных курсов."""
    
    @classmethod
    def get_course(cls, course_id: int) -> Optional[Dict]:
        """Получить курс из кеша."""
        key = f"{RedisCache.COURSE_PREFIX}{course_id}"
        return RedisCache.get(key)
    
    @classmethod
    def set_course(cls, course_id: int, course_data: Any, timeout: int = 1800) -> bool:
        """Сохранить курс в кеш на 30 минут."""
        key = f"{RedisCache.COURSE_PREFIX}{course_id}"
        return RedisCache.set(key, course_data, timeout)
    
    @classmethod
    def delete_course(cls, course_id: int) -> bool:
        """Удалить курс из кеша."""
        key = f"{RedisCache.COURSE_PREFIX}{course_id}"
        return RedisCache.delete(key)
    
    @classmethod
    def get_course_modules(cls, course_id: int) -> Optional[List]:
        """Получить модули курса из кеша."""
        key = f"{RedisCache.COURSE_PREFIX}{course_id}:modules"
        return RedisCache.get(key)
    
    @classmethod
    def set_course_modules(cls, course_id: int, modules_data: List, timeout: int = 1800) -> bool:
        """Сохранить модули курса в кеш."""
        key = f"{RedisCache.COURSE_PREFIX}{course_id}:modules"
        return RedisCache.set(key, modules_data, timeout)
    
    @classmethod
    def clear_course_cache(cls, course_id: int) -> bool:
        """Очистить весь кеш курса."""
        pattern = f"{RedisCache.COURSE_PREFIX}{course_id}*"
        return RedisCache.clear_pattern(pattern)


class UserCache:
    """Специализированный класс для кеширования данных пользователей."""
    
    @classmethod
    def get_user_profile(cls, user_id: int) -> Optional[Dict]:
        """Получить профиль пользователя из кеша."""
        key = f"{RedisCache.USER_PREFIX}{user_id}:profile"
        return RedisCache.get(key)
    
    @classmethod
    def set_user_profile(cls, user_id: int, profile_data: Any, timeout: int = 900) -> bool:
        """Сохранить профиль пользователя в кеш на 15 минут."""
        key = f"{RedisCache.USER_PREFIX}{user_id}:profile"
        return RedisCache.set(key, profile_data, timeout)
    
    @classmethod
    def get_user_progress(cls, user_id: int, course_id: int) -> Optional[Dict]:
        """Получить прогресс пользователя по курсу."""
        key = f"{RedisCache.USER_PREFIX}{user_id}:progress:{course_id}"
        return RedisCache.get(key)
    
    @classmethod
    def set_user_progress(cls, user_id: int, course_id: int, progress_data: Any, timeout: int = 600) -> bool:
        """Сохранить прогресс пользователя по курсу."""
        key = f"{RedisCache.USER_PREFIX}{user_id}:progress:{course_id}"
        return RedisCache.set(key, progress_data, timeout)
    
    @classmethod
    def clear_user_cache(cls, user_id: int) -> bool:
        """Очистить весь кеш пользователя."""
        pattern = f"{RedisCache.USER_PREFIX}{user_id}*"
        return RedisCache.clear_pattern(pattern)


class APICache:
    """Кеширование API ответов."""
    
    @classmethod
    def get_api_response(cls, endpoint: str, params: str = "") -> Optional[Any]:
        """Получить кешированный API ответ."""
        key = f"{RedisCache.API_PREFIX}{endpoint}:{hash(params)}"
        return RedisCache.get(key)
    
    @classmethod
    def set_api_response(cls, endpoint: str, params: str, response_data: Any, timeout: int = 300) -> bool:
        """Сохранить API ответ в кеш."""
        key = f"{RedisCache.API_PREFIX}{endpoint}:{hash(params)}"
        return RedisCache.set(key, response_data, timeout)


class GenerationCache:
    """Кеширование данных генерации курсов."""
    
    @classmethod
    def get_generation_status(cls, task_id: str) -> Optional[Dict]:
        """Получить статус генерации курса."""
        key = f"{RedisCache.GENERATION_PREFIX}{task_id}:status"
        return RedisCache.get(key)
    
    @classmethod
    def set_generation_status(cls, task_id: str, status_data: Dict, timeout: int = 3600) -> bool:
        """Сохранить статус генерации курса на 1 час."""
        key = f"{RedisCache.GENERATION_PREFIX}{task_id}:status"
        return RedisCache.set(key, status_data, timeout)
    
    @classmethod
    def get_generation_result(cls, task_id: str) -> Optional[Dict]:
        """Получить результат генерации курса."""
        key = f"{RedisCache.GENERATION_PREFIX}{task_id}:result"
        return RedisCache.get(key)
    
    @classmethod
    def set_generation_result(cls, task_id: str, result_data: Dict, timeout: int = 7200) -> bool:
        """Сохранить результат генерации курса на 2 часа."""
        key = f"{RedisCache.GENERATION_PREFIX}{task_id}:result"
        return RedisCache.set(key, result_data, timeout)