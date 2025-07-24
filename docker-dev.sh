#!/bin/bash

# Скрипт для управления Docker окружением разработки
# Поддерживает полное разделение фронтенда и бэкенда

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_help() {
    echo -e "${BLUE}Управление Docker окружением AiKademiya${NC}"
    echo ""
    echo "Использование: ./docker-dev.sh [КОМАНДА]"
    echo ""
    echo "Команды:"
    echo "  up       - Запустить все сервисы"
    echo "  down     - Остановить все сервисы"
    echo "  restart  - Перезапустить все сервисы"
    echo "  logs     - Показать логи всех сервисов"
    echo "  backend  - Показать только логи бэкенда"
    echo "  frontend - Показать только логи фронтенда"
    echo "  build    - Пересобрать образы"
    echo "  clean    - Очистить все (volumes, images, containers)"
    echo "  status   - Показать статус сервисов"
    echo "  shell    - Войти в shell Django контейнера"
    echo "  migrate  - Выполнить миграции Django"
    echo "  help     - Показать эту справку"
    echo ""
    echo "Сервисы будут доступны по адресам:"
    echo "  - Фронтенд: ${GREEN}http://localhost:5173${NC}"
    echo "  - Django API: ${GREEN}http://localhost:8000/api${NC}"
    echo "  - Django Admin: ${GREEN}http://localhost:8000/admin${NC}"
    echo "  - API Docs: ${GREEN}http://localhost:8000/api/schema/swagger-ui/${NC}"
    echo "  - Temporal UI: ${GREEN}http://localhost:8080${NC}"
}

case "$1" in
    up)
        echo -e "${GREEN}🚀 Запуск всех сервисов...${NC}"
        docker-compose up -d
        echo -e "${GREEN}✅ Все сервисы запущены!${NC}"
        echo ""
        echo -e "📱 Фронтенд: ${BLUE}http://localhost:5173${NC}"
        echo -e "🔧 Django API: ${BLUE}http://localhost:8000/api${NC}"
        echo -e "⚙️  Django Admin: ${BLUE}http://localhost:8000/admin${NC}"
        echo -e "📚 API Docs: ${BLUE}http://localhost:8000/api/schema/swagger-ui/${NC}"
        echo -e "⏱️  Temporal UI: ${BLUE}http://localhost:8080${NC}"
        ;;
    down)
        echo -e "${YELLOW}🛑 Остановка всех сервисов...${NC}"
        docker-compose down
        echo -e "${GREEN}✅ Все сервисы остановлены!${NC}"
        ;;
    restart)
        echo -e "${YELLOW}🔄 Перезапуск всех сервисов...${NC}"
        docker-compose down
        docker-compose up -d
        echo -e "${GREEN}✅ Все сервисы перезапущены!${NC}"
        ;;
    logs)
        echo -e "${BLUE}📋 Показываю логи всех сервисов...${NC}"
        docker-compose logs -f
        ;;
    backend)
        echo -e "${BLUE}📋 Показываю логи Django бэкенда...${NC}"
        docker-compose logs -f web
        ;;
    frontend)
        echo -e "${BLUE}📋 Показываю логи Vue фронтенда...${NC}"
        docker-compose logs -f frontend
        ;;
    build)
        echo -e "${YELLOW}🔨 Пересборка образов...${NC}"
        docker-compose build --no-cache
        echo -e "${GREEN}✅ Образы пересобраны!${NC}"
        ;;
    clean)
        echo -e "${RED}🧹 Очистка всех Docker ресурсов...${NC}"
        read -p "Вы уверены? Это удалит все volumes, образы и контейнеры! (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            docker-compose down -v
            docker system prune -a -f
            echo -e "${GREEN}✅ Очистка завершена!${NC}"
        else
            echo -e "${YELLOW}❌ Очистка отменена${NC}"
        fi
        ;;
    status)
        echo -e "${BLUE}📊 Статус сервисов:${NC}"
        docker-compose ps
        ;;
    shell)
        echo -e "${BLUE}🐚 Вход в Django shell...${NC}"
        docker-compose exec web python aikademiya/manage.py shell
        ;;
    migrate)
        echo -e "${BLUE}🗃️  Выполнение миграций Django...${NC}"
        docker-compose exec web python aikademiya/manage.py migrate
        echo -e "${GREEN}✅ Миграции выполнены!${NC}"
        ;;
    help|--help|-h)
        print_help
        ;;
    "")
        print_help
        ;;
    *)
        echo -e "${RED}❌ Неизвестная команда: $1${NC}"
        echo ""
        print_help
        exit 1
        ;;
esac