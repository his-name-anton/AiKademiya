# Docker Development для AiKademiya

## 🏗️ Архитектура

Проект настроен для **полного разделения фронтенда и бэкенда**:

- **Backend**: Django REST API (контейнер `web`) - порт 8000
- **Frontend**: Vue.js + Vite (контейнер `frontend`) - порт 5173  
- **Database**: PostgreSQL (контейнер `db`) - порт 5432
- **Temporal**: Workflow engine (порт 7233) + UI (порт 8080)

## 🚀 Быстрый старт

### 1. Запуск всех сервисов

```bash
# Простой способ - используйте готовый скрипт
./docker-dev.sh up

# Или напрямую через docker-compose
docker-compose up -d
```

### 2. Доступ к сервисам

После запуска будут доступны:

- 📱 **Vue Frontend**: http://localhost:5173
- 🔧 **Django API**: http://localhost:8000/api  
- ⚙️ **Django Admin**: http://localhost:8000/admin
- 📚 **API Documentation**: http://localhost:8000/api/schema/swagger-ui/
- ⏱️ **Temporal UI**: http://localhost:8080

### 3. Первоначальная настройка

```bash
# Выполнить миграции базы данных
./docker-dev.sh migrate

# Или напрямую
docker-compose exec web python aikademiya/manage.py migrate

# Создать суперпользователя (опционально)
docker-compose exec web python aikademiya/manage.py createsuperuser
```

## 🛠️ Команды для разработки

### Управление сервисами

```bash
./docker-dev.sh up        # Запустить все сервисы
./docker-dev.sh down      # Остановить все сервисы  
./docker-dev.sh restart   # Перезапустить все сервисы
./docker-dev.sh status    # Показать статус сервисов
```

### Логи и отладка

```bash
./docker-dev.sh logs      # Логи всех сервисов
./docker-dev.sh backend   # Только логи Django
./docker-dev.sh frontend  # Только логи Vue
./docker-dev.sh shell     # Django shell
```

### Обслуживание

```bash
./docker-dev.sh build     # Пересобрать образы
./docker-dev.sh migrate   # Выполнить миграции
./docker-dev.sh clean     # Полная очистка (осторожно!)
```

## 🔧 Конфигурация

### Переменные окружения

**Frontend** (`.env.development`):
```bash
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_TITLE=AiKademiya
NODE_ENV=development
```

**Backend** (docker-compose.yml):
```yaml
environment:
  POSTGRES_HOST: db
  DJANGO_DEBUG: "True"
  TEMPORAL_ADDRESS: temporal:7233
```

### Сеть

Все контейнеры находятся в одной Docker сети, что позволяет им обращаться друг к другу по именам сервисов:

- Frontend → Backend: `http://web:8000/api` (внутри Docker)
- Frontend → Backend: `http://localhost:8000/api` (из браузера)

## 📊 Структура сервисов

```yaml
services:
  web:           # Django API
  frontend:      # Vue.js App  
  db:           # PostgreSQL для Django
  temporal:     # Temporal Workflow
  postgresql:   # PostgreSQL для Temporal
  temporal-ui:  # Temporal UI
```

## 🔥 Hot Reload

- **Vue.js**: Автоматический hot reload при изменении файлов
- **Django**: Автоматический перезапуск при изменении Python файлов
- **Volumes**: Код монтируется в контейнеры для мгновенных изменений

## 🐛 Решение проблем

### Frontend не может подключиться к API

1. Проверьте, что Django сервер запущен:
   ```bash
   ./docker-dev.sh status
   ```

2. Проверьте логи бэкенда:
   ```bash
   ./docker-dev.sh backend
   ```

3. Убедитесь в правильных CORS настройках в Django

### База данных не доступна

```bash
# Проверьте статус контейнера БД
docker-compose ps db

# Перезапустите только БД
docker-compose restart db

# Проверьте логи БД
docker-compose logs db
```

### Temporal не работает

```bash
# Проверьте все Temporal сервисы
docker-compose ps temporal temporal-ui postgresql

# Перезапустите Temporal стек
docker-compose restart temporal temporal-ui postgresql
```

### Полная перезагрузка

```bash
# Остановить всё
./docker-dev.sh down

# Пересобрать образы
./docker-dev.sh build  

# Запустить заново
./docker-dev.sh up
```

## 📈 Продакшен

Для продакшена используйте отдельные Dockerfile и docker-compose.prod.yml с:

- Vue build в статические файлы
- Nginx для статики и проксирования
- PostgreSQL как отдельный сервис
- Переменные окружения для продакшена

## 🔗 Полезные ссылки

- [Docker Compose документация](https://docs.docker.com/compose/)
- [Vue.js в Docker](https://vuejs.org/guide/scaling-up/tooling.html#docker)
- [Django в Docker](https://docs.djangoproject.com/en/stable/howto/deployment/docker/)
- [Temporal Docker](https://docs.temporal.io/docs/server/docker)

## 💡 Советы

1. **Используйте `./docker-dev.sh`** - он содержит все нужные команды
2. **Мониторьте логи** при разработке новых функций
3. **Регулярно делайте `docker-dev.sh restart`** после больших изменений
4. **Делайте бэкапы БД** перед экспериментами с миграциями