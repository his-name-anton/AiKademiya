#!/bin/bash

# Скрипт для запуска режима разработки
# Django бэкенд на :8000 и Vue фронтенд на :5173

echo "Запуск среды разработки..."
echo "Django API: http://localhost:8000"
echo "Vue App: http://localhost:5173"
echo ""

# Запуск Django в фоне
echo "Запуск Django сервера..."
cd aikademiya
python manage.py runserver &
DJANGO_PID=$!

# Запуск Vue dev сервера в фоне
echo "Запуск Vue dev сервера..."
cd ../frontend
npm run dev &
VUE_PID=$!

# Функция для остановки серверов
cleanup() {
    echo ""
    echo "Остановка серверов..."
    kill $DJANGO_PID 2>/dev/null
    kill $VUE_PID 2>/dev/null
    exit 0
}

# Перехват Ctrl+C
trap cleanup INT

echo "Оба сервера запущены. Нажмите Ctrl+C для остановки."
echo "Django PID: $DJANGO_PID"
echo "Vue PID: $VUE_PID"

# Ожидание
wait