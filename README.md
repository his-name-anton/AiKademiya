# AiKademiya

Educational course generation platform.

## Local development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run services with Docker Compose (PostgreSQL and n8n):
   ```bash
   docker-compose up
   ```
3. Apply migrations and create a superuser:
   ```bash
   docker-compose exec web python aikademiya/manage.py migrate
   docker-compose exec web python aikademiya/manage.py createsuperuser
   ```
4. Access the site at <http://localhost:8000> and n8n at <http://localhost:5678>.

The project connects to PostgreSQL using environment variables defined in
`docker-compose.yml`. n8n can be configured with your OpenAI API key to test
requests to the model.
