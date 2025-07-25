# Redis в AI Akademiya - Быстрый старт

## Что добавлено

✅ **Redis сервис** в Docker Compose  
✅ **Кеширование API** курсов, пользователей, категорий  
✅ **Rate limiting** для защиты от спама  
✅ **Сессии в Redis** для масштабируемости  
✅ **Мониторинг** через админ панель  
✅ **Автоматическая очистка** кеша при изменении данных  

## Запуск

```bash
# Поднять все сервисы включая Redis
docker-compose up -d

# Проверить что Redis запустился
docker-compose ps redis
docker-compose logs redis
```

## Использование

### Проверка работы

```bash
# Статистика кеша
docker exec aikademiya-backend python manage.py clear_cache --stats

# Тестовый запрос к API (должен попасть в кеш)
curl http://localhost:8000/api/categories/
```

### Админка Redis

1. Войдите в админку: http://localhost:8000/admin/
2. Перейдите в: http://localhost:8000/admin/redis-stats/
3. Просматривайте статистику и управляйте кешем

### Управление кешем

```bash
# Очистить весь кеш
docker exec aikademiya-backend python manage.py clear_cache --all

# Очистить кеш курсов
docker exec aikademiya-backend python manage.py clear_cache --pattern "course:*"

# Очистить кеш пользователя
docker exec aikademiya-backend python manage.py clear_cache --pattern "user:123:*"
```

## Что кешируется

| Данные | Время жизни | Триггер очистки |
|--------|-------------|-----------------|
| Список курсов | 10 мин | Изменение курса |
| Детали курса | 30 мин | Изменение курса/модуля |
| Категории | 30 мин | Изменение категории |
| Профиль пользователя | 15 мин | Изменение профиля |
| Статус генерации | 1 час | Завершение генерации |

## Rate Limiting

- **API запросы**: 100/час с IP
- **Аутентификация**: 20/час с IP  
- **Генерация курсов**: 10/час на пользователя
- **Смена пароля**: 20/час с IP

## Мониторинг

### В браузере
- Админка: http://localhost:8000/admin/redis-stats/

### Через API заголовки
- `X-Cache-Hits` - попадания в кеш
- `X-Cache-Misses` - промахи кеша  
- `X-Response-Time` - время ответа

### Логи производительности

```bash
# Медленные запросы (>1сек) в логах Django
docker-compose logs web | grep "Медленный запрос"
```

## Конфигурация Redis

В `docker-compose.yml`:
- **Память**: 512MB с LRU политикой
- **Персистентность**: AOF включен
- **Сеть**: Только внутри Docker

Переменная окружения:
```
REDIS_URL=redis://redis:6379/1
```

## Troubleshooting

### Redis недоступен
```bash
# Проверка контейнера
docker-compose ps redis
docker-compose logs redis

# Перезапуск
docker-compose restart redis
```

### Переполнение памяти
```bash
# Очистка кеша
docker exec aikademiya-backend python manage.py clear_cache --all

# Увеличение лимита в docker-compose.yml
command: redis-server --maxmemory 1024mb
```

### Низкая производительность
1. Проверьте Hit Rate в админке (должен быть >80%)
2. Увеличьте время жизни кеша для статических данных
3. Оптимизируйте запросы к БД

## Дополнительно

📖 **Полная документация**: [`docs/redis-integration.md`](docs/redis-integration.md)

🔧 **Утилиты для разработки**:
```python
from core.redis_utils import CourseCache, UserCache
from core.decorators import cache_api_response
```

🚀 **Готово к продакшену** с мониторингом и масштабированием