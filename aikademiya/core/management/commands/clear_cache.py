"""
Django команда для управления Redis кешем.
Использование: python manage.py clear_cache [--pattern PATTERN] [--all]
"""

from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from core.redis_utils import RedisCache


class Command(BaseCommand):
    help = 'Управление Redis кешем: очистка по паттерну или полная очистка'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pattern',
            type=str,
            help='Паттерн ключей для удаления (например: "course:*")',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Очистить весь кеш',
        )
        parser.add_argument(
            '--stats',
            action='store_true',
            help='Показать статистику кеша',
        )

    def handle(self, *args, **options):
        if options['stats']:
            self.show_cache_stats()
            return

        if options['all']:
            self.clear_all_cache()
        elif options['pattern']:
            self.clear_cache_pattern(options['pattern'])
        else:
            self.stdout.write(
                self.style.WARNING(
                    'Укажите --pattern для очистки по паттерну или --all для полной очистки'
                )
            )

    def clear_all_cache(self):
        """Очистить весь кеш."""
        try:
            cache.clear()
            self.stdout.write(
                self.style.SUCCESS('Весь кеш успешно очищен')
            )
        except Exception as e:
            raise CommandError(f'Ошибка очистки кеша: {e}')

    def clear_cache_pattern(self, pattern):
        """Очистить кеш по паттерну."""
        try:
            result = RedisCache.clear_pattern(pattern)
            if result:
                self.stdout.write(
                    self.style.SUCCESS(f'Кеш по паттерну "{pattern}" очищен')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Не удалось очистить кеш по паттерну "{pattern}"')
                )
        except Exception as e:
            raise CommandError(f'Ошибка очистки кеша по паттерну: {e}')

    def show_cache_stats(self):
        """Показать статистику кеша."""
        try:
            from django_redis import get_redis_connection
            redis_conn = get_redis_connection("default")
            
            info = redis_conn.info()
            
            self.stdout.write(self.style.SUCCESS('=== Статистика Redis ==='))
            self.stdout.write(f"Версия Redis: {info.get('redis_version', 'N/A')}")
            self.stdout.write(f"Используемая память: {info.get('used_memory_human', 'N/A')}")
            self.stdout.write(f"Пиковая память: {info.get('used_memory_peak_human', 'N/A')}")
            self.stdout.write(f"Количество ключей: {info.get('db0', {}).get('keys', 0) if 'db0' in info else 0}")
            self.stdout.write(f"Попадания в кеш: {info.get('keyspace_hits', 0)}")
            self.stdout.write(f"Промахи кеша: {info.get('keyspace_misses', 0)}")
            
            # Подсчет hit rate
            hits = info.get('keyspace_hits', 0)
            misses = info.get('keyspace_misses', 0)
            if hits + misses > 0:
                hit_rate = (hits / (hits + misses)) * 100
                self.stdout.write(f"Hit rate: {hit_rate:.2f}%")
            
        except Exception as e:
            raise CommandError(f'Ошибка получения статистики: {e}')