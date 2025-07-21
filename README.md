# AiKademiya

Educational course generation platform.

## Local development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Install Node dependencies and build Tailwind CSS:
   ```bash
   npm install
   npx tailwindcss -i assets/css/tailwind.css -o static/css/tailwind.css --minify
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

### Email setup

Configure SMTP credentials via the following environment variables if you want
real emails to be sent:

```
EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS,
DEFAULT_FROM_EMAIL
```

During local development you can run a fake SMTP server, for example with
`python -m smtpd -n -c DebuggingServer localhost:1025`, and set
`EMAIL_PORT=1025`.

The project connects to PostgreSQL using environment variables defined in
`docker-compose.yml`. n8n can be configured with your OpenAI API key to test
requests to the model.
