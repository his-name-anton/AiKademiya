# Инструкции по тестированию исправлений авторизации

## Тесты для проверки исправления проблемы

### 🔥 ОСНОВНОЙ ТЕСТ: Обновление страницы
1. **Войдите в систему** через `/login`
2. **Перейдите в личный кабинет** (любую страницу с `requiresAuth: true`)
3. **Обновите страницу** (F5, Ctrl+R или кнопка обновления)
4. **✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:** Вы остаетесь в личном кабинете, НЕ перебрасывает на главную/логин

### 📋 Дополнительные тесты

#### Тест 1: Прямой переход по URL
1. Войдите в систему
2. Скопируйте URL личного кабинета (например `/dashboard` или `/profile`)
3. Откройте новую вкладку и вставьте этот URL
4. **✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:** Попадаете в личный кабинет без перенаправления на логин

#### Тест 2: Перезапуск браузера
1. Войдите в систему
2. Полностью закройте браузер
3. Откройте браузер снова
4. Перейдите на сайт
5. **✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:** Если токены не истекли, попадаете в личный кабинет

#### Тест 3: Истекший access token, валидный refresh token
1. Войдите в систему
2. В консоли браузера выполните:
   ```javascript
   // Устанавливаем истекший access token
   localStorage.setItem('access_token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMDAwMDAwLCJpYXQiOjE2MDAwMDAwMDAsImp0aSI6InRlc3QiLCJ1c2VyX2lkIjoxfQ.test')
   ```
3. Обновите страницу
4. **✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:** Токен автоматически обновится, пользователь останется авторизованным

#### Тест 4: Неактивность 24 часа (имитация)
1. Войдите в систему
2. В консоли браузера:
   ```javascript
   // Получаем auth store
   const { useAuthStore } = window.Pinia
   const authStore = useAuthStore()
   
   // Имитируем 24 часа неактивности
   authStore.lastActivityTime = Date.now() - (24 * 60 * 60 * 1000 + 1000)
   ```
3. Выполните любое действие (клик, движение мыши)
4. **✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:** Пользователь автоматически разлогинивается

### 📊 Проверка логов в консоли

При корректной работе в консоли должны быть логи:
```
Initializing auth store...
Starting auth initialization...
Stored tokens: {hasAccessToken: true, hasRefreshToken: true}
Tokens found, checking validity...
Fetching user profile to verify token...
Profile fetched successfully, user is authenticated
Auth initialization completed successfully
Auth store initialized successfully
Mounting Vue app...
Auth initialization confirmed in App.vue
```

### 🚨 Признаки проблем

Если видите в консоли:
- `Auth not initialized in router, waiting...` - нормально при первой загрузке
- `Token refresh failed during initialization` - проблема с backend или истекшие токены
- `Failed to fetch profile during initialization` - проблема с API или невалидные токены
- Бесконечные циклы логов - проблема с инициализацией

### 🔧 Отладка проблем

#### Проблема: Пользователь все еще выбрасывается
1. Откройте DevTools → Application → Local Storage
2. Проверьте наличие `access_token` и `refresh_token`
3. Проверьте консоль на ошибки
4. Убедитесь, что backend доступен

#### Проблема: Бесконечные редиректы
1. Очистите localStorage: `localStorage.clear()`
2. Перезагрузите страницу
3. Войдите заново

#### Проблема: Токены не обновляются
1. Проверьте, что `refresh_token` валидный
2. Проверьте доступность API endpoint `/v1/auth/token/refresh/`
3. Проверьте консоль на ошибки 401/403

### ⚡ Быстрая проверка исправления

Выполните в консоли браузера:
```javascript
// Проверка инициализации
console.log('Auth initialized:', authStore.isInitialized)
console.log('User authenticated:', authStore.isAuthenticated)
console.log('Access token:', !!authStore.accessToken)
console.log('Refresh token:', !!authStore.refreshToken)
```

Все значения должны быть `true` для авторизованного пользователя.

### 📞 Если ничего не работает

1. Убедитесь, что внесены ВСЕ изменения из `AUTH_FIXES_SUMMARY.md`
2. Перезапустите dev server: `npm run dev`
3. Очистите кэш браузера и localStorage
4. Проверьте, что backend работает и отвечает на API запросы