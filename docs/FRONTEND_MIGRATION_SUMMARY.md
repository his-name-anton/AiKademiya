# Миграция фронтенда с Django на Vue.js

## Обзор

Данный проект был успешно переведен с серверного рендеринга Django на современное SPA приложение на Vue.js 3 с TypeScript.

## Что было сделано

### 1. Страницы аутентификации (Vue.js)
- **LoginPage.vue** - Страница входа в систему
- **RegisterPage.vue** - Страница регистрации  
- **ForgotPasswordPage.vue** - Восстановление пароля

### 2. Пользовательские страницы (Vue.js)
- **ProfilePage.vue** - Профиль пользователя с возможностью редактирования
- **SettingsPage.vue** - Настройки аккаунта, языка, уведомлений
- **LearnPage.vue** - Страница обучения с курсами

### 3. Базовые компоненты
- **BaseButton.vue** - Универсальная кнопка
- **BaseInput.vue** - Универсальное поле ввода
- **FormAlert.vue** - Компонент уведомлений в формах

### 4. Роутинг и навигация
- Обновлен **router/index.ts** с маршрутами для всех страниц
- Добавлены защищенные маршруты (requiresAuth)
- Добавлены маршруты только для гостей (requiresGuest)
- Обновлена **MainNavbar.vue** с поддержкой аутентификации

### 5. Управление состоянием
- **Pinia stores** для аутентификации
- **TypeScript типы** для всех данных
- **API клиенты** для работы с бэкендом

### 6. Django интеграция
- Обновлены Django views для перенаправления на Vue приложение
- Сохранены API endpoints для взаимодействия с фронтендом
- Базовый `VueAppView` для рендеринга Vue приложения

## Структура проекта

```
frontend/
├── src/
│   ├── api/              # API клиенты
│   │   ├── auth.ts
│   │   ├── client.ts
│   │   └── courses.ts
│   ├── components/       # Переиспользуемые компоненты
│   │   ├── common/
│   │   │   ├── BaseButton.vue
│   │   │   ├── BaseInput.vue
│   │   │   └── FormAlert.vue
│   │   └── layout/
│   │       └── MainNavbar.vue
│   ├── pages/           # Страницы приложения
│   │   ├── auth/
│   │   │   ├── LoginPage.vue
│   │   │   ├── RegisterPage.vue
│   │   │   └── ForgotPasswordPage.vue
│   │   ├── ProfilePage.vue
│   │   ├── SettingsPage.vue
│   │   ├── LearnPage.vue
│   │   └── IndexPage.vue
│   ├── router/          # Vue Router конфигурация
│   │   └── index.ts
│   ├── stores/          # Pinia состояние
│   │   ├── auth.ts
│   │   └── courses.ts
│   ├── types/           # TypeScript типы
│   │   └── index.ts
│   ├── App.vue          # Главный компонент
│   └── main.ts          # Точка входа
└── package.json         # Зависимости
```

## Технологический стек

### Frontend
- **Vue.js 3** - Основной фреймворк
- **TypeScript** - Типизация
- **Vite** - Сборщик
- **Vue Router** - Роутинг
- **Pinia** - Управление состоянием
- **Tailwind CSS** - Стили
- **Flowbite Vue** - UI компоненты
- **Vue Toastification** - Уведомления
- **Axios** - HTTP клиент

### Backend (Django)
- **Django REST Framework** - API
- **Django CORS Headers** - CORS поддержка
- Сохранены все существующие API endpoints

## Преимущества нового решения

1. **Современный UX** - Одностраничное приложение без перезагрузок
2. **Типизация** - TypeScript обеспечивает безопасность типов
3. **Компонентность** - Переиспользуемые Vue компоненты
4. **Реактивность** - Автоматическое обновление интерфейса
5. **Производительность** - Быстрая навигация, ленивая загрузка
6. **Разделение ответственности** - Четкое разделение фронтенда и бэкенда

## Маршруты

| Маршрут | Компонент | Защищен | Описание |
|---------|-----------|---------|----------|
| `/` | IndexPage | Нет | Главная страница |
| `/login` | LoginPage | Гость | Вход в систему |
| `/register` | RegisterPage | Гость | Регистрация |
| `/forgot-password` | ForgotPasswordPage | Гость | Восстановление пароля |
| `/generate` | GeneratePage | Да | Создание курса |
| `/learn` | LearnPage | Да | Обучение |
| `/profile` | ProfilePage | Да | Профиль пользователя |
| `/settings` | SettingsPage | Да | Настройки |

## Следующие шаги

1. **Интеграция с Django API** - Подключить реальные API endpoints
2. **Тестирование** - Написать unit и integration тесты
3. **Оптимизация** - Добавить code splitting и оптимизацию bundle
4. **PWA** - Превратить в прогрессивное веб-приложение
5. **i18n** - Добавить поддержку интернационализации

## Запуск проекта

### Разработка
```bash
cd frontend
npm install
npm run dev
```

### Продакшен
```bash
cd frontend
npm run build
```

Собранные файлы будут в `frontend/dist/` и автоматически подключены к Django.