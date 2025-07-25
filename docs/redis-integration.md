# Интеграция Redis в проект AI Akademiya

## Обзор

Redis интегрирован в проект для решения следующих задач:

- **Кеширование данных** - курсы, модули, главы, профили пользователей
- **Сессии пользователей** - хранение в Redis для масштабируемости
- **Rate limiting** - ограничение частоты запросов к API
- **Временное хранение** - статусы генерации курсов, промежуточные результаты
- **Производительность** - ускорение API запросов через кеширование

## Конфигурация

### Docker Compose

Redis запускается как отдельный сервис в `docker-compose.yml`:

```yaml
redis:
  image: redis:7-alpine
  container_name: aikademiya-redis
  ports:
    - "6379:6379"
  volumes:
    - redis_data:/data
  command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru
  networks:
    - default
```

### Настройки Django

В `settings.py` настроен кеш и сессии:

```python
# Redis configuration
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/1")

# Cache configuration with Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
        "KEY_PREFIX": "aikademiya",
        "TIMEOUT": 300,
    }
}

# Session storage в Redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

## Структура кеша

### Префиксы ключей

- `course:*` - данные курсов
- `user:*` - данные пользователей
- `api:*` - кешированные API ответы
- `generation:*` - статусы генерации курсов
- `stats:*` - статистические данные

### Время жизни кеша

- **Курсы**: 30 минут (часто обновляемые)
- **Категории**: 30 минут (редко изменяются)
- **Профили пользователей**: 15 минут
- **API ответы**: 5-10 минут
- **Генерация курсов**: 1-2 часа

## Использование

### Основные утилиты

#### RedisCache - базовый класс

```python
from core.redis_utils import RedisCache

# Сохранить данные
RedisCache.set("my_key", {"data": "value"}, timeout=300)

# Получить данные
data = RedisCache.get("my_key", default={})

# Удалить ключ
RedisCache.delete("my_key")

# Очистить по паттерну
RedisCache.clear_pattern("course:*")
```

#### CourseCache - для курсов

```python
from core.redis_utils import CourseCache

# Кешировать курс
CourseCache.set_course(course_id, course_data)

# Получить курс из кеша
cached_course = CourseCache.get_course(course_id)

# Кешировать модули курса
CourseCache.set_course_modules(course_id, modules_data)

# Очистить весь кеш курса
CourseCache.clear_course_cache(course_id)
```

#### UserCache - для пользователей

```python
from core.redis_utils import UserCache

# Кешировать профиль
UserCache.set_user_profile(user_id, profile_data)

# Получить профиль
profile = UserCache.get_user_profile(user_id)

# Кешировать прогресс по курсу
UserCache.set_user_progress(user_id, course_id, progress_data)

# Очистить кеш пользователя
UserCache.clear_user_cache(user_id)
```

### Декораторы кеширования

#### Для API представлений

```python
from core.decorators import cache_api_response, cache_course_data, invalidate_course_cache

class CourseListView(generics.ListAPIView):
    @cache_api_response(timeout=600)  # 10 минут
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CourseDetailView(generics.RetrieveUpdateAPIView):
    @cache_course_data(timeout=1800)  # 30 минут
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @invalidate_course_cache
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
```

#### Rate Limiting

```python
from core.decorators import api_rate_limit, generation_rate_limit

class CourseGenerationView(APIView):
    @generation_rate_limit  # 10 генераций в час на пользователя
    def post(self, request):
        # логика генерации
        pass

@api_rate_limit  # 100 запросов в час с IP
def some_api_view(request):
    pass
```

### Автоматическая очистка кеша

Настроены Django сигналы для автоматической очистки:

```python
# При изменении курса
@receiver(post_save, sender='courses.Course')
def invalidate_course_cache_on_save(sender, instance, **kwargs):
    CourseCache.clear_course_cache(instance.id)
    RedisCache.clear_pattern("api_response:*courses*")
```

## Мониторинг

### Django Admin

Доступна админ панель Redis по адресу: `/admin/redis-stats/`

Возможности:
- Просмотр статистики Redis
- Мониторинг использования памяти
- Hit/Miss ratio
- Управление кешем (очистка)

### Команды управления

```bash
# Показать статистику
python manage.py clear_cache --stats

# Очистить весь кеш
python manage.py clear_cache --all

# Очистить по паттерну
python manage.py clear_cache --pattern "course:*"
python manage.py clear_cache --pattern "user:123:*"
```

### Middleware мониторинга

Автоматически добавляются заголовки:
- `X-Cache-Hits` - количество попаданий в кеш
- `X-Cache-Misses` - количество промахов
- `X-Response-Time` - время ответа

## Стратегии кеширования

### 1. Cache-Aside (Lazy Loading)

Используется для данных курсов и пользователей:

```python
def get_course(course_id):
    # Проверяем кеш
    cached = CourseCache.get_course(course_id)
    if cached:
        return cached
    
    # Загружаем из БД
    course = Course.objects.get(id=course_id)
    
    # Сохраняем в кеш
    CourseCache.set_course(course_id, course)
    return course
```

### 2. Write-Through

Для критических данных (профили, прогресс):

```python
def update_user_profile(user_id, data):
    # Обновляем БД
    user = User.objects.get(id=user_id)
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    
    # Обновляем кеш
    UserCache.set_user_profile(user_id, user)
```

### 3. Cache Invalidation

При изменении данных через сигналы Django:

```python
@receiver(post_save, sender=Course)
def invalidate_course_cache(sender, instance, **kwargs):
    CourseCache.clear_course_cache(instance.id)
```

## Оптимизация производительности

### Рекомендации

1. **Мониторинг Hit Rate** - должен быть > 80%
2. **Размер ключей** - используйте короткие, но понятные ключи
3. **TTL политика** - устанавливайте разумные времена жизни
4. **Память** - мониторьте использование, настройте `maxmemory-policy`

### Настройка памяти

В `docker-compose.yml`:

```yaml
command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru
```

Политики освобождения:
- `allkeys-lru` - удаляет наименее используемые ключи
- `allkeys-lfu` - удаляет наименее часто используемые
- `volatile-ttl` - удаляет ключи с ближайшим TTL

## Безопасность

### Защита Redis

1. **Сеть** - Redis доступен только внутри Docker сети
2. **Аутентификация** - не настроена (внутренняя сеть)
3. **Шифрование** - TLS не настроено (внутренняя связь)

### Предотвращение атак

- Rate limiting через `django-ratelimit`
- Валидация ключей кеша
- Ограничение размера данных

## Backup и восстановление

### Автоматический backup

Redis настроен с `appendonly yes` для сохранности данных.

### Ручной backup

```bash
# В контейнере Redis
docker exec aikademiya-redis redis-cli BGSAVE

# Копирование файла
docker cp aikademiya-redis:/data/dump.rdb ./backup/
```

### Восстановление

```bash
# Остановить контейнер
docker-compose stop redis

# Восстановить файл
docker cp ./backup/dump.rdb aikademiya-redis:/data/

# Запустить контейнер
docker-compose start redis
```

## Troubleshooting

### Частые проблемы

1. **Redis недоступен**
   ```bash
   # Проверить статус
   docker-compose ps redis
   
   # Логи
   docker-compose logs redis
   ```

2. **Память переполнена**
   ```bash
   # Очистить кеш
   python manage.py clear_cache --all
   
   # Увеличить лимит памяти в docker-compose.yml
   ```

3. **Низкий Hit Rate**
   - Проверить TTL ключей
   - Оптимизировать стратегию кеширования
   - Увеличить время жизни кеша

### Логирование

Включено логирование в `core/redis_utils.py` и middleware.

Уровни логов:
- `DEBUG` - операции с кешем
- `WARNING` - медленные запросы
- `ERROR` - ошибки Redis

## Масштабирование

### Горизонтальное масштабирование

Для продакшена рекомендуется:

1. **Redis Cluster** - распределение данных
2. **Redis Sentinel** - высокая доступность
3. **Отдельные инстансы** - для разных типов данных

### Вертикальное масштабирование

- Увеличение памяти контейнера
- Оптимизация конфигурации Redis
- Использование Redis 7+ для лучшей производительности

## Заключение

Redis успешно интегрирован для:
- ✅ Кеширования данных курсов и пользователей
- ✅ Хранения сессий
- ✅ Rate limiting API
- ✅ Ускорения генерации курсов
- ✅ Мониторинга производительности

Система готова к продакшену с настроенным мониторингом и управлением.