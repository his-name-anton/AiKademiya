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
2. Run services with Docker Compose (PostgreSQL):
   ```bash
   docker-compose up
   ```
3. Apply migrations and create a superuser:
   ```bash
   docker-compose exec web python aikademiya/manage.py makemigrations
   docker-compose exec web python aikademiya/manage.py migrate
   docker-compose exec web python aikademiya/manage.py createsuperuser
   ```
4. 4. Access the site at <http://localhost:8000>.

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
`docker-compose.yml`.

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


## Temporal workflows

The project uses [Temporal](https://temporal.io) for background course
generation. To run the worker locally:

```bash
pip install -r requirements.txt
python scripts/temporal_worker.py
```

Start a Temporal server separately (for example via Docker) and set the
`TEMPORAL_ADDRESS` environment variable if it is not running on the default
`localhost:7233` address. Generated workflows can be inspected at the Temporal
Web UI on port `8088`.

The worker listens on the `course-task-queue` queue. New course generation can be
triggered via the API endpoints:

- `POST /api/create_course/` with JSON `{"topic": "..."}`
- `GET  /api/status/<workflow_id>/`
- `POST /api/confirm/<workflow_id>/` to start generation after review
- `POST /api/next/<workflow_id>/` to request the next chapte

These return the workflow ID and allow checking its status and result.
These return the workflow ID and allow checking progress or driving the
interactive generation process.

### AI configuration

AI models and prompt templates are managed via the Django admin interface. Use
the `AIModel`, `AITaskType` and `PromptTemplate` models to configure which
OpenAI model and prompt should be used for each generation step. Requests and
responses are logged in `AIRequestLog` for auditing.