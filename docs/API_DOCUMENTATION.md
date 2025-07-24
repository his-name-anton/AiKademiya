# AI Akademiya REST API Documentation

## Overview

This document describes the REST API for AI Akademiya - an AI-powered educational platform for generating courses. The API is built using Django REST Framework and provides endpoints for user management, course creation, and quiz functionality.

## Base URL

```
http://localhost:8000/api/v1/
```

## Authentication

The API uses JWT (JSON Web Token) authentication. After login, you'll receive access and refresh tokens that must be included in subsequent requests.

### Headers

```
Authorization: Bearer <access_token>
Content-Type: application/json
```

## API Documentation

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://localhost:8000/api/schema/redoc/`

## Endpoints

### Authentication (`/api/v1/auth/`)

#### Register User
```
POST /api/v1/auth/register/
```

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "occupation": "student",
    "sex": "male"
}
```

**Response:**
```json
{
    "message": "Пользователь успешно зарегистрирован",
    "user": {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "student"
    },
    "tokens": {
        "refresh": "refresh_token_here",
        "access": "access_token_here"
    }
}
```

#### Login
```
POST /api/v1/auth/login/
```

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "securepassword123"
}
```

#### Refresh Token
```
POST /api/v1/auth/token/refresh/
```

**Request Body:**
```json
{
    "refresh": "refresh_token_here"
}
```

#### Logout
```
POST /api/v1/auth/logout/
```

**Request Body:**
```json
{
    "refresh_token": "refresh_token_here"
}
```

#### Get User Profile
```
GET /api/v1/auth/profile/
```

#### Update User Profile
```
PATCH /api/v1/auth/profile/
```

**Request Body:**
```json
{
    "first_name": "Updated Name",
    "occupation": "employed"
}
```

#### Change Password
```
POST /api/v1/auth/change-password/
```

**Request Body:**
```json
{
    "old_password": "oldpassword",
    "new_password": "newpassword123",
    "new_password_confirm": "newpassword123"
}
```

### Courses (`/api/v1/courses/`)

#### List Courses
```
GET /api/v1/courses/
```

**Query Parameters:**
- `level`: Filter by difficulty level (`beginner`, `intermediate`, `advanced`)
- `language`: Filter by language (e.g., `ru`, `en`)
- `category`: Filter by category ID
- `search`: Search in title and description
- `my_courses`: Show only user's courses (`true`/`false`)

**Response:**
```json
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Python для начинающих",
            "description": "Основы программирования на Python",
            "level": "beginner",
            "language": "ru",
            "is_public": true,
            "created_by": "user@example.com",
            "category": "Программирование",
            "modules_count": 5,
            "total_chapters": 20,
            "created_at": "2024-01-01T12:00:00Z"
        }
    ]
}
```

#### Create Course
```
POST /api/v1/courses/
```

**Request Body:**
```json
{
    "title": "Новый курс",
    "description": "Описание курса",
    "level": "beginner",
    "goal": "Цель обучения",
    "language": "ru",
    "is_public": true,
    "category_id": 1
}
```

#### Get Course Details
```
GET /api/v1/courses/{id}/
```

**Response:**
```json
{
    "id": 1,
    "title": "Python для начинающих",
    "description": "Основы программирования на Python",
    "level": "beginner",
    "goal": "Изучить основы Python",
    "language": "ru",
    "is_public": true,
    "created_by": {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "category": {
        "id": 1,
        "name": "Программирование"
    },
    "modules": [
        {
            "id": 1,
            "title": "Введение",
            "short_description": "Основы Python",
            "index": 1,
            "chapters": [
                {
                    "id": 1,
                    "title": "Что такое Python",
                    "index": 1,
                    "summary": "Введение в Python"
                }
            ],
            "chapters_count": 3
        }
    ],
    "modules_count": 5,
    "total_chapters": 20,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

#### Update Course
```
PATCH /api/v1/courses/{id}/
```

#### Delete Course
```
DELETE /api/v1/courses/{id}/
```

#### List Course Categories
```
GET /api/v1/courses/categories/
```

### AI Course Generation

#### Generate Course
```
POST /api/v1/courses/generate/
```

**Request Body:**
```json
{
    "topic": "Основы машинного обучения",
    "level": "intermediate",
    "goal": "Изучить основные алгоритмы ML",
    "language": "ru",
    "category_id": 2
}
```

**Response:**
```json
{
    "workflow_id": "course-uuid-here",
    "message": "Генерация курса запущена",
    "topic": "Основы машинного обучения"
}
```

#### Check Generation Status
```
GET /api/v1/courses/generate/{workflow_id}/status/
```

#### Confirm Generated Course
```
POST /api/v1/courses/generate/{workflow_id}/confirm/
```

#### Generate Next Chapter
```
POST /api/v1/courses/generate/{workflow_id}/next-chapter/
```

### Modules and Chapters

#### Get Module Details
```
GET /api/v1/courses/modules/{id}/
```

#### Get Chapter Details
```
GET /api/v1/courses/chapters/{id}/
```

**Response:**
```json
{
    "id": 1,
    "title": "Введение в Python",
    "content": "Python - это высокоуровневый язык программирования...",
    "index": 1,
    "summary": "Краткое введение в Python",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

### Quizzes (`/api/v1/quizzes/`)

#### Get Chapter Questions
```
GET /api/v1/quizzes/chapters/{chapter_id}/questions/
```

#### Create Question (for course owners)
```
POST /api/v1/quizzes/chapters/{chapter_id}/questions/
```

**Request Body:**
```json
{
    "text": "Что такое Python?",
    "options_list": [
        "Язык программирования",
        "База данных",
        "Операционная система",
        "Веб-браузер"
    ],
    "correct_answer": "Язык программирования"
}
```

#### Get Quiz Questions (without answers)
```
GET /api/v1/quizzes/chapters/{chapter_id}/quiz/
```

**Response:**
```json
{
    "chapter_id": 1,
    "chapter_title": "Введение в Python",
    "questions": [
        {
            "id": 1,
            "text": "Что такое Python?",
            "options_list": [
                "Язык программирования",
                "База данных",
                "Операционная система",
                "Веб-браузер"
            ]
        }
    ],
    "total_questions": 1
}
```

#### Answer Single Question
```
POST /api/v1/quizzes/questions/{question_id}/answer/
```

**Request Body:**
```json
{
    "answer": "Язык программирования"
}
```

**Response:**
```json
{
    "question_id": 1,
    "user_answer": "Язык программирования",
    "is_correct": true,
    "correct_answer": "Язык программирования"
}
```

#### Take Chapter Quiz
```
POST /api/v1/quizzes/chapters/{chapter_id}/take-quiz/
```

**Request Body:**
```json
{
    "answers": [
        {
            "question_id": 1,
            "answer": "Язык программирования"
        },
        {
            "question_id": 2,
            "answer": "Неправильный ответ"
        }
    ]
}
```

**Response:**
```json
{
    "chapter_id": 1,
    "total_questions": 2,
    "correct_answers": 1,
    "score_percentage": 50.0,
    "passed": false,
    "questions_results": [
        {
            "question_id": 1,
            "user_answer": "Язык программирования",
            "is_correct": true,
            "correct_answer": "Язык программирования"
        },
        {
            "question_id": 2,
            "user_answer": "Неправильный ответ",
            "is_correct": false,
            "correct_answer": "Правильный ответ"
        }
    ]
}
```

## Error Responses

All endpoints return appropriate HTTP status codes and error messages:

### Validation Errors (400)
```json
{
    "field_name": ["Error message"]
}
```

### Authentication Errors (401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### Permission Errors (403)
```json
{
    "error": "У вас нет прав на выполнение этого действия"
}
```

### Not Found Errors (404)
```json
{
    "detail": "Not found."
}
```

## Usage Examples

### Complete User Flow Example

1. **Register a user:**
```bash
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "student@example.com",
    "password": "password123",
    "password_confirm": "password123",
    "first_name": "Alex",
    "last_name": "Smith"
  }'
```

2. **Login to get tokens:**
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "student@example.com",
    "password": "password123"
  }'
```

3. **List available courses:**
```bash
curl -X GET http://localhost:8000/api/v1/courses/ \
  -H "Authorization: Bearer <access_token>"
```

4. **Generate a new course:**
```bash
curl -X POST http://localhost:8000/api/v1/courses/generate/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Django REST API",
    "level": "intermediate",
    "goal": "Научиться создавать REST API с Django"
  }'
```

5. **Take a quiz:**
```bash
curl -X POST http://localhost:8000/api/v1/quizzes/chapters/1/take-quiz/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": 1, "answer": "Мой ответ"}
    ]
  }'
```

## Features Converted to REST API

✅ **User Management**
- Registration and authentication with JWT
- Profile management
- Password change functionality

✅ **Course Management**
- CRUD operations for courses
- Course categories
- Module and chapter access
- Permission-based access control

✅ **AI Course Generation**
- Integration with Temporal workflows
- Status tracking for course generation
- Step-by-step course creation

✅ **Quiz System**
- Question management
- Quiz taking with instant feedback
- Chapter-based quizzes with scoring

✅ **API Documentation**
- Automatic OpenAPI schema generation
- Swagger UI and ReDoc interfaces
- Comprehensive endpoint documentation

✅ **Security & Permissions**
- JWT authentication
- Role-based permissions
- CORS support for frontend integration

## Next Steps

1. **Frontend Integration**: Use these API endpoints to build a modern frontend (React, Vue.js, etc.)
2. **Mobile App**: The REST API can be easily consumed by mobile applications
3. **Third-party Integrations**: Other systems can integrate with the platform via the API
4. **Microservices**: The API can be extended to support microservices architecture

The platform is now fully converted to a modern REST API architecture while maintaining all original functionality!