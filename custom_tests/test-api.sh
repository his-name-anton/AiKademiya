#!/bin/bash

# Простой тест API endpoints
echo "🧪 Тестирование AiKademiya API..."

API_BASE="http://localhost:8000"

echo ""
echo "📡 Проверка доступности Django API..."
curl -s -o /dev/null -w "Status: %{http_code}\n" $API_BASE/api/

echo ""
echo "📡 Проверка API Root..."
curl -s $API_BASE/api/ | python -m json.tool

echo ""
echo "📡 Проверка API Schema..."
curl -s -o /dev/null -w "API Schema Status: %{http_code}\n" $API_BASE/api/schema/

echo ""
echo "📡 Проверка Swagger UI..."
curl -s -o /dev/null -w "Swagger UI Status: %{http_code}\n" $API_BASE/api/schema/swagger-ui/

echo ""
echo "📡 Проверка Django Admin..."
curl -s -o /dev/null -w "Django Admin Status: %{http_code}\n" $API_BASE/admin/

echo ""
echo "🏁 Тест завершен!"
echo ""
echo "Если все статусы 200, то API работает корректно."
echo "Если 500 - возможно нужно выполнить миграции: ./docker-dev.sh migrate"