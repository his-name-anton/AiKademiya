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
   npx @tailwindcss/cli -i ./assets/css/input.css -o ./static/css/tailwind.css
   ```
2. Run services with Docker Compose (PostgreSQL and n8n):
   ```bash
   docker-compose up
   ```
3. Apply migrations and create a superuser:
   ```bash
   docker-compose exec web python aikademiya/manage.py makemigrations
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

## Django apps

The codebase is organised into dedicated Django applications:

| App | Purpose |
|-----|---------|
| **users** | Authentication, OAuth, roles, subscription status and user profiles |
| **courses** | Courses, modules and chapters of learning content |
| **quizzes** | Questions, answers and test evaluation logic |
| **progress** | Tracks completion of courses and chapters |
| **generation** | Stores history of content generation requests |
| **billing** | Subscription plans and payment processing |
| **catalog** | Public catalogue of courses with filters and ratings |
| **adminpanel** | Admin UI, reports and moderation tools |
| **core** | Shared utilities, abstract models and middleware |
