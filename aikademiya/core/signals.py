"""
Сигналы Django для автоматической очистки кеша при изменении моделей.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .redis_utils import CourseCache, UserCache, RedisCache

User = get_user_model()


@receiver(post_save, sender='courses.Course')
def invalidate_course_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша курса при сохранении."""
    CourseCache.clear_course_cache(instance.id)
    # Очищаем также общий кеш списка курсов
    RedisCache.clear_pattern("api_response:*courses*")


@receiver(post_delete, sender='courses.Course')
def invalidate_course_cache_on_delete(sender, instance, **kwargs):
    """Очистка кеша курса при удалении."""
    CourseCache.clear_course_cache(instance.id)
    RedisCache.clear_pattern("api_response:*courses*")


@receiver(post_save, sender='courses.Module')
def invalidate_module_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша курса при изменении модуля."""
    CourseCache.clear_course_cache(instance.course.id)


@receiver(post_delete, sender='courses.Module')
def invalidate_module_cache_on_delete(sender, instance, **kwargs):
    """Очистка кеша курса при удалении модуля."""
    CourseCache.clear_course_cache(instance.course.id)


@receiver(post_save, sender='courses.Chapter')
def invalidate_chapter_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша курса при изменении главы."""
    CourseCache.clear_course_cache(instance.module.course.id)


@receiver(post_delete, sender='courses.Chapter')
def invalidate_chapter_cache_on_delete(sender, instance, **kwargs):
    """Очистка кеша курса при удалении главы."""
    CourseCache.clear_course_cache(instance.module.course.id)


@receiver(post_save, sender=User)
def invalidate_user_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша пользователя при изменении профиля."""
    UserCache.clear_user_cache(instance.id)


@receiver(post_save, sender='courses.CourseCategory')
def invalidate_category_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша категорий при изменении."""
    RedisCache.clear_pattern("api_response:*categories*")


@receiver(post_delete, sender='courses.CourseCategory')
def invalidate_category_cache_on_delete(sender, instance, **kwargs):
    """Очистка кеша категорий при удалении."""
    RedisCache.clear_pattern("api_response:*categories*")


# Сигналы для прогресса пользователя
@receiver(post_save, sender='progress.UserProgress')
def invalidate_progress_cache_on_save(sender, instance, **kwargs):
    """Очистка кеша прогресса при изменении."""
    if hasattr(instance, 'user_id') and hasattr(instance, 'course_id'):
        UserCache.set_user_progress(
            instance.user_id, 
            instance.course_id, 
            None  # Очищаем кеш, установив None
        )