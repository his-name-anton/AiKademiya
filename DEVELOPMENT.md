# Руководство по разработке AiKademiya

## Архитектура проекта

Проект использует архитектуру разделения фронтенда и бэкенда:

- **Бэкенд**: Django REST API (порт 8000)
- **Фронтенд**: Vue.js + Vite (порт 5173)

## Быстрый старт

### Автоматический запуск (рекомендуемый)

```bash
# Запуск обоих серверов одной командой
./dev.sh
```

### Ручной запуск

#### 1. Запуск Django API сервера

```bash
cd aikademiya
python manage.py runserver
```

Django API будет доступно по адресу: http://localhost:8000

#### 2. Запуск Vue.js фронтенда

```bash
cd frontend
npm run dev
```

Vue приложение будет доступно по адресу: http://localhost:5173

## Режимы работы

### Режим разработки (Development)

В режиме разработки:
- Django использует `templates/index.html` 
- Vue код загружается напрямую с Vite dev сервера (`http://localhost:5173/src/main.ts`)
- Hot reload работает для Vue компонентов
- API запросы проксируются на Django сервер

### Режим продакшена (Production)

В режиме продакшена:
- Vue приложение собирается в `static/frontend/`
- Django отдает собранные статические файлы
- Используется один домен для фронтенда и API

## Структура проекта

```
aikademiya/
├── aikademiya/          # Django проект
│   ├── settings.py      # Настройки Django
│   └── urls.py          # URL маршруты
├── frontend/            # Vue.js приложение
│   ├── src/             # Исходный код Vue
│   ├── index.html       # HTML шаблон для Vite
│   ├── vite.config.js   # Конфигурация Vite
│   └── package.json     # NPM зависимости
├── templates/           # Django шаблоны
│   └── index.html       # Основной шаблон (использует Vue)
├── static/              # Статические файлы Django
└── dev.sh              # Скрипт для разработки
```

## API Endpoints

Django предоставляет REST API по следующим путям:

- `/api/v1/auth/` - Аутентификация
- `/api/v1/courses/` - Курсы  
- `/api/v1/quizzes/` - Тесты
- `/admin/` - Django Admin
- `/api/schema/swagger-ui/` - API документация

## Решение проблем

### Ошибка 404 для main.js

Если вы видите ошибку `404 Not Found` для `http://localhost:5173/main.js`, это означает что:

1. **Проблема**: Django использует неправильный путь в `templates/index.html`
2. **Решение**: Путь исправлен на `/src/main.ts` в этом проекте

### CORS ошибки

Если Vue не может обращаться к Django API:

1. Убедитесь, что `localhost:5173` добавлен в `CORS_ALLOWED_ORIGINS` в `settings.py`
2. Проверьте, что Django сервер запущен на порту 8000

### Vite не запускается

```bash
cd frontend
npm install  # Переустановить зависимости
npm run dev
```

## Рекомендации

### Если нужен только API бэкенд

Если вы хотите использовать Django только как API:

1. Разрабатывайте Vue приложение на `http://localhost:5173`
2. Используйте Django API на `http://localhost:8000/api/`
3. В продакшене разместите фронтенд и бэкенд на разных доменах/поддоменах

### Если нужна интеграция

Если вы хотите, чтобы Django отдавал Vue приложение:

1. Используйте `templates/index.html` для разработки
2. Настройте `vite build` для сборки в `static/frontend/`
3. Django будет отдавать собранные файлы в продакшене

## Команды для разработки

```bash
# Установка зависимостей
pip install -r requirements.txt
cd frontend && npm install

# Запуск тестов Django
cd aikademiya && python manage.py test

# Запуск линтера Vue
cd frontend && npm run lint

# Сборка для продакшена
cd frontend && npm run build

# Миграции базы данных
cd aikademiya && python manage.py migrate
```