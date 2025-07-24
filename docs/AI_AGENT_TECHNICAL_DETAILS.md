# Технические детали реализации AI агента для генерации обучающих материалов

## 📋 Содержание
1. [Детальный анализ Temporal AI Agent](#детальный-анализ-temporal-ai-agent)
2. [Django + Vue архитектура](#django--vue-архитектура)
3. [Система управления промптами](#система-управления-промптами)
4. [Конкретная реализация для обучающих материалов](#конкретная-реализация)
5. [Расширенные инструменты образовательного контента](#расширенные-инструменты)
6. [API спецификация Django REST](#api-спецификация-django-rest)
7. [Развертывание и мониторинг](#развертывание)

---

## 🔍 Детальный анализ Temporal AI Agent

### Как работает Workflow

Основной workflow (`AgentGoalWorkflow`) следует следующей логике:

1. **Инициализация**: Загрузка цели агента и MCP инструментов
2. **Основной цикл**: Ожидание сигналов от пользователя
3. **Обработка ввода**: Валидация и вызов LLM
4. **Выполнение инструментов**: Запуск необходимых activities
5. **Подтверждение**: Получение разрешения пользователя на выполнение

### Структура данных из проекта:

```python
# Из models/data_types.py
class ConversationHistory(TypedDict):
    messages: List[Dict[str, Any]]

class NextStep(TypedDict):
    next: str  # "question", "tool_call", "end"
    response: str
    
class ToolData(TypedDict, total=False):
    next: NextStep
    tool: str
    args: Dict[str, Any]
    response: str
    force_confirm: bool
```

### Ключевые сигналы Workflow:

```python
@workflow.signal
async def user_prompt(self, prompt: str) -> None:
    """Получение ввода от пользователя"""
    self.prompt_queue.append(prompt)

@workflow.signal  
async def confirm(self, confirmed: bool) -> None:
    """Подтверждение выполнения инструмента"""
    self.confirmed = confirmed

@workflow.signal
async def end_chat(self) -> None:
    """Завершение сессии"""
    self.chat_ended = True
```

---

## 💻 Примеры кода из проекта

### 1. Определение цели агента (из `goals/finance.py`)

```python
goal_fin_check_account_balances = AgentGoal(
    id="goal_fin_check_account_balances",
    category_tag="fin",
    agent_name="Account Balances",
    agent_friendly_description="Check your account balances in Checking, Savings, etc.",
    tools=[
        tool_registry.financial_check_account_is_valid,
        tool_registry.financial_get_account_balances,
    ],
    description="The user wants to check their account balances at the bank or financial institution...",
    starter_prompt=starter_prompt_generic,
    example_conversation_history="..."
)
```

### 2. Реализация инструмента (из `tools/fin/`)

```python
async def financial_check_account_is_valid(email: str, account_number: str) -> dict:
    """Проверка валидности аккаунта"""
    # Симуляция проверки в базе данных
    if "@" in email and len(account_number) >= 5:
        return {
            "status": "account valid",
            "email": email,
            "account_number": account_number
        }
    else:
        raise ValueError("Invalid account credentials")
```

### 3. Activity для выполнения инструментов

```python
@activity.defn
async def execute_tool(self, tool_name: str, tool_args: dict) -> dict:
    """Выполнение инструмента с обработкой ошибок"""
    try:
        tool_function = get_tool_function(tool_name)
        result = await tool_function(**tool_args)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

---

## 🎓 Конкретная реализация для обучающих материалов

### 1. Workflow для генерации курсов

```python
from datetime import timedelta
from typing import Dict, List, Optional
from temporalio import workflow
from models.education_types import Course, Lesson, Exercise, UserProfile

@workflow.defn
class LearningMaterialWorkflow:
    """Workflow для генерации обучающих материалов"""
    
    def __init__(self):
        self.user_profile: Optional[UserProfile] = None
        self.course: Optional[Course] = None
        self.current_lesson_index: int = 0
        self.generated_lessons: List[Lesson] = []
        self.exercises: List[Exercise] = []
        self.chat_ended: bool = False
        self.waiting_for_confirmation: bool = False
        
    @workflow.run
    async def run(self, initial_request: str) -> Course:
        """Основной метод генерации курса"""
        
        # 1. Сбор информации о пользователе
        await self.collect_user_profile()
        
        # 2. Создание структуры курса
        self.course = await workflow.execute_activity(
            create_course_outline,
            args=[initial_request, self.user_profile],
            schedule_to_close_timeout=timedelta(minutes=5)
        )
        
        # 3. Основной цикл генерации контента
        while not self.chat_ended:
            await workflow.wait_condition(
                lambda: self.should_generate_content() or self.chat_ended
            )
            
            if self.should_generate_content():
                await self.generate_next_lesson()
        
        return self.course
    
    async def collect_user_profile(self):
        """Сбор профиля пользователя через диалог"""
        questions = [
            "Какой у вас уровень знаний по этой теме?",
            "Сколько времени вы готовы уделять обучению?", 
            "Предпочитаете теорию или практику?",
            "Какова ваша цель изучения?"
        ]
        
        answers = []
        for question in questions:
            answer = await self.ask_question(question)
            answers.append(answer)
            
        self.user_profile = await workflow.execute_activity(
            create_user_profile,
            args=[answers],
            schedule_to_close_timeout=timedelta(minutes=2)
        )
    
    async def generate_next_lesson(self):
        """Генерация следующего урока"""
        if self.current_lesson_index < len(self.course.lesson_titles):
            lesson = await workflow.execute_activity(
                generate_lesson_content,
                args=[
                    self.course.lesson_titles[self.current_lesson_index],
                    self.user_profile,
                    self.course.topic
                ],
                schedule_to_close_timeout=timedelta(minutes=3)
            )
            
            self.generated_lessons.append(lesson)
            self.current_lesson_index += 1
            
            # Генерация упражнения для урока
            exercise = await workflow.execute_activity(
                create_lesson_exercise,
                args=[lesson, self.user_profile],
                schedule_to_close_timeout=timedelta(minutes=2)
            )
            
            self.exercises.append(exercise)
    
    # Сигналы
    @workflow.signal
    async def user_response(self, response: str):
        """Получение ответа от пользователя"""
        self.current_user_response = response
        
    @workflow.signal  
    async def generate_more_content(self):
        """Запрос на генерацию дополнительного контента"""
        self.content_requested = True
        
    @workflow.signal
    async def complete_course(self):
        """Завершение создания курса"""
        self.chat_ended = True
```

### 2. Activities для генерации контента

```python
from temporalio import activity
from typing import List, Dict, Any
import json
from litellm import completion

class EducationActivities:
    
    @activity.defn
    async def create_course_outline(
        self, 
        topic: str, 
        user_profile: UserProfile
    ) -> Course:
        """Создание структуры курса"""
        
        prompt = f"""
        Создай детальную структуру курса на тему "{topic}" для пользователя со следующим профилем:
        - Уровень: {user_profile.level}
        - Время обучения: {user_profile.time_commitment} 
        - Стиль: {user_profile.learning_style}
        - Цель: {user_profile.goal}
        
        Верни JSON со следующей структурой:
        {{
            "title": "Название курса",
            "description": "Описание курса",
            "duration_weeks": число_недель,
            "lesson_titles": ["Урок 1", "Урок 2", ...],
            "learning_objectives": ["Цель 1", "Цель 2", ...],
            "prerequisites": ["Требование 1", ...]
        }}
        """
        
        response = await completion(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.llm_key
        )
        
        course_data = json.loads(response.choices[0].message.content)
        return Course(**course_data, topic=topic)
    
    @activity.defn
    async def generate_lesson_content(
        self,
        lesson_title: str,
        user_profile: UserProfile, 
        course_topic: str
    ) -> Lesson:
        """Генерация контента урока"""
        
        prompt = f"""
        Создай подробный урок на тему "{lesson_title}" в рамках курса "{course_topic}".
        
        Профиль ученика:
        - Уровень: {user_profile.level}
        - Стиль обучения: {user_profile.learning_style}
        
        Структура урока должна включать:
        1. Введение и мотивация (почему это важно)
        2. Основной материал с примерами
        3. Практические советы
        4. Резюме ключевых моментов
        5. Что изучать далее
        
        Объем: 1500-2000 слов, понятный язык, много примеров.
        
        Верни JSON:
        {{
            "title": "{lesson_title}",
            "introduction": "...",
            "content_sections": [
                {{"heading": "...", "content": "..."}},
                ...
            ],
            "key_takeaways": ["...", "..."],
            "next_steps": "..."
        }}
        """
        
        response = await completion(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.llm_key
        )
        
        lesson_data = json.loads(response.choices[0].message.content)
        return Lesson(**lesson_data)
    
    @activity.defn
    async def create_lesson_exercise(
        self,
        lesson: Lesson,
        user_profile: UserProfile
    ) -> Exercise:
        """Создание практического упражнения"""
        
        prompt = f"""
        Создай практическое упражнение для урока "{lesson.title}".
        
        Уровень сложности: {user_profile.level}
        Стиль обучения: {user_profile.learning_style}
        
        Упражнение должно включать:
        1. Четкую постановку задачи
        2. Пошаговые инструкции
        3. Примеры решения (если применимо)
        4. Критерии оценки
        5. Подсказки для затруднений
        
        Верни JSON:
        {{
            "title": "...",
            "description": "...",
            "instructions": ["Шаг 1", "Шаг 2", ...],
            "example_solution": "...",
            "evaluation_criteria": ["...", "..."],
            "hints": ["...", "..."],
            "estimated_time_minutes": число
        }}
        """
        
        response = await completion(
            model=self.llm_model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.llm_key
        )
        
        exercise_data = json.loads(response.choices[0].message.content)
        return Exercise(**exercise_data, lesson_id=lesson.title)
```

### 3. Модели данных

```python
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

class LearningLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate" 
    ADVANCED = "advanced"

class LearningStyle(Enum):
    THEORETICAL = "theoretical"
    PRACTICAL = "practical"
    MIXED = "mixed"

@dataclass
class UserProfile:
    level: LearningLevel
    time_commitment: str  # "5 hours per week"
    learning_style: LearningStyle
    goal: str
    preferred_language: str = "ru"

@dataclass
class ContentSection:
    heading: str
    content: str

@dataclass
class Lesson:
    title: str
    introduction: str
    content_sections: List[ContentSection]
    key_takeaways: List[str]
    next_steps: str
    estimated_duration_minutes: int = 30

@dataclass
class Exercise:
    title: str
    description: str
    instructions: List[str]
    example_solution: Optional[str]
    evaluation_criteria: List[str]
    hints: List[str]
    estimated_time_minutes: int
    lesson_id: str

@dataclass
class Course:
    title: str
    description: str
    topic: str
    duration_weeks: int
    lesson_titles: List[str]
    learning_objectives: List[str]
    prerequisites: List[str]
    lessons: List[Lesson] = None
    exercises: List[Exercise] = None
```

### 4. Goals для образовательного агента

```python
from typing import List
import tools.education_tools as edu_tools
from models.tool_definitions import AgentGoal

# Цель создания полного курса
goal_create_full_course = AgentGoal(
    id="goal_create_full_course",
    category_tag="education",
    agent_name="Course Creator", 
    agent_friendly_description="Создание полного интерактивного курса на любую тему",
    tools=[
        edu_tools.collect_user_requirements,
        edu_tools.generate_course_outline,
        edu_tools.create_lesson_content,
        edu_tools.generate_exercises,
        edu_tools.review_and_refine
    ],
    description="""
    Я помогу вам создать персонализированный обучающий курс на любую тему.
    Для создания качественного курса мне нужно:
    1. Понять ваши цели и уровень знаний
    2. Создать структуру курса
    3. Сгенерировать контент уроков
    4. Добавить практические упражнения
    5. Настроить курс под ваши потребности
    """,
    starter_prompt="Привет! Я создам для вас персонализированный курс. О чем вы хотели бы узнать?",
    example_conversation_history="""
    user: Хочу изучить основы машинного обучения
    agent: Отлично! Расскажите о своем опыте в программировании и математике
    user: Знаю Python на среднем уровне, математику помню со школы
    agent: Понятно. Сколько времени готовы уделять обучению в неделю?
    user: Примерно 6-8 часов
    agent: Создаю для вас 10-недельный курс "Основы машинного обучения для Python-разработчиков"...
    """
)

# Цель создания отдельного урока
goal_create_lesson = AgentGoal(
    id="goal_create_lesson", 
    category_tag="education",
    agent_name="Lesson Creator",
    agent_friendly_description="Создание отдельного урока на конкретную тему",
    tools=[
        edu_tools.analyze_topic,
        edu_tools.structure_lesson,
        edu_tools.generate_content,
        edu_tools.add_examples
    ],
    description="Создание подробного урока на конкретную тему с примерами и упражнениями",
    starter_prompt="На какую тему создать урок? Укажите уровень сложности."
)

education_goals = [
    goal_create_full_course,
    goal_create_lesson,
    # Другие образовательные цели...
]
```

---

## 🎯 Примеры промптов и взаимодействий

### 1. Промпт для анализа требований пользователя

```python
USER_REQUIREMENTS_PROMPT = """
Проанализируй запрос пользователя на создание обучающего курса и извлеки ключевую информацию.

Запрос: "{user_request}"

Дополнительная информация от пользователя:
{additional_info}

Определи и верни JSON со следующими полями:
{{
    "topic": "основная тема курса",
    "estimated_level": "beginner/intermediate/advanced", 
    "preferred_duration": "количество недель или уроков",
    "learning_goals": ["цель 1", "цель 2", ...],
    "specific_requirements": ["требование 1", "требование 2", ...],
    "missing_information": ["что нужно уточнить у пользователя"],
    "suggested_questions": ["вопрос 1", "вопрос 2", ...]
}}

Если информации недостаточно для создания курса, укажи это в missing_information.
"""
```

### 2. Промпт для генерации урока

```python
LESSON_GENERATION_PROMPT = """
Создай подробный урок на тему "{lesson_topic}" в рамках курса "{course_title}".

Контекст курса:
- Общая тема: {course_topic}
- Целевая аудитория: {target_audience}
- Уровень: {level}
- Номер урока: {lesson_number} из {total_lessons}

Предыдущие уроки: {previous_lessons}

Требования к уроку:
1. Логическая связь с предыдущими уроками
2. Четкая структура с введением, основной частью, заключением
3. Практические примеры и упражнения
4. Объем 1500-2500 слов
5. Понятный язык без избыточной терминологии

Структура ответа в JSON:
{{
    "lesson_title": "{lesson_topic}",
    "learning_objectives": ["цель 1", "цель 2", ...],
    "prerequisites": ["что должен знать ученик"],
    "introduction": {{
        "hook": "интересный факт или вопрос для привлечения внимания",
        "overview": "обзор того, что изучим в уроке",
        "relevance": "почему это важно знать"
    }},
    "main_content": [
        {{
            "section_title": "Название раздела",
            "content": "подробное объяснение",
            "examples": ["пример 1", "пример 2"],
            "key_points": ["ключевая идея 1", "ключевая идея 2"]
        }}
    ],
    "practical_exercise": {{
        "title": "Название упражнения",
        "description": "что нужно сделать",
        "steps": ["шаг 1", "шаг 2", ...],
        "expected_outcome": "что должно получиться"
    }},
    "summary": {{
        "key_takeaways": ["главная идея 1", "главная идея 2"],
        "next_lesson_preview": "что изучим в следующем уроке"
    }},
    "additional_resources": ["ссылка или название ресурса"],
    "estimated_duration_minutes": 45
}}
"""
```

### 3. Пример диалога с агентом

```
👤 Пользователь: Хочу создать курс по веб-разработке для начинающих

🤖 Агент: Отлично! Я помогу создать курс по веб-разработке. Чтобы сделать его максимально полезным, ответьте на несколько вопросов:

1. Есть ли у вас опыт программирования? 
2. Сколько времени готовы уделять обучению в неделю?
3. Какую цель преследуете - изменить карьеру, дополнить навыки или изучить для хобби?

👤 Пользователь: Программирование изучал в университете, но это было 5 лет назад. Могу уделять 8-10 часов в неделю. Хочу сменить карьеру на IT.

🤖 Агент: Понятно! Основы есть, но нужно освежить. Для смены карьеры создам практический курс с портфолио проектов.

Какой стек технологий вас больше интересует:
- Frontend (HTML, CSS, JavaScript, React)  
- Backend (Node.js, Python, базы данных)
- Fullstack (все вместе)

👤 Пользователь: Fullstack, хочу понимать весь процесс

🤖 Агент: Создаю 16-недельный курс "Fullstack веб-разработчик: от основ до первого проекта"

📋 Структура курса:
**Недели 1-4: Frontend основы**
- HTML5 и семантическая разметка
- CSS3, Flexbox, Grid
- Адаптивная верстка
- Основы JavaScript

**Недели 5-8: Продвинутый Frontend**  
- JavaScript ES6+, DOM манипуляции
- React основы и хуки
- State management
- API интеграция

**Недели 9-12: Backend разработка**
- Node.js и Express
- Базы данных (MongoDB, PostgreSQL)
- Аутентификация и авторизация
- RESTful API

**Недели 13-16: Финальный проект**
- Планирование fullstack приложения
- Разработка frontend и backend
- Деплой и CI/CD
- Портфолио и резюме

Каждую неделю включает:
- 2-3 урока с теорией (3-4 часа)
- Практические задания (4-5 часов)  
- Мини-проект (1-2 часа)

Начинаем с первого урока?

👤 Пользователь: Да, давайте начнем!

🤖 Агент: 🚀 **Урок 1: Современная веб-разработка - обзор и инструменты**

*Генерирую подробный контент урока...*

📚 **Цели урока:**
- Понять экосистему современной веб-разработки
- Настроить среду разработки
- Создать первую HTML страницу

**Введение:**
Веб-разработка кардинально изменилась за последние 5 лет...

[Подробный контент урока с примерами кода, упражнениями и ссылками]
```

---

## 🌐 API спецификация

### Основные эндпоинты

```python
from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI(title="Learning AI Agent API")

# Запуск нового курса
@app.post("/courses/create")
async def create_course(request: CreateCourseRequest):
    """Создание нового курса"""
    workflow_id = f"course_{uuid.uuid4()}"
    
    await temporal_client.start_workflow(
        LearningMaterialWorkflow.run,
        args=[request.topic, request.user_profile],
        id=workflow_id,
        task_queue="education-tasks"
    )
    
    return {"course_id": workflow_id, "status": "started"}

# Получение статуса курса
@app.get("/courses/{course_id}/status")
async def get_course_status(course_id: str):
    """Получение текущего статуса генерации курса"""
    handle = temporal_client.get_workflow_handle(course_id)
    
    try:
        status = await handle.query(
            LearningMaterialWorkflow.get_status
        )
        return status
    except Exception as e:
        raise HTTPException(status_code=404, detail="Course not found")

# Отправка сообщения в workflow
@app.post("/courses/{course_id}/message")
async def send_message(course_id: str, message: MessageRequest):
    """Отправка сообщения пользователя в workflow"""
    handle = temporal_client.get_workflow_handle(course_id)
    
    await handle.signal(
        LearningMaterialWorkflow.user_response,
        message.content
    )
    
    return {"status": "message_sent"}

# Получение сгенерированного контента
@app.get("/courses/{course_id}/content")
async def get_course_content(course_id: str):
    """Получение всего контента курса"""
    handle = temporal_client.get_workflow_handle(course_id)
    
    course_data = await handle.query(
        LearningMaterialWorkflow.get_course_data
    )
    
    return course_data

# Модели данных для API
class CreateCourseRequest(BaseModel):
    topic: str
    user_profile: UserProfile
    
class MessageRequest(BaseModel):
    content: str
    message_type: str = "user_input"

class CourseStatus(BaseModel):
    status: str  # "collecting_requirements", "generating_outline", "creating_lessons", "completed"
    progress_percentage: int
    current_step: str
    lessons_generated: int
    total_lessons: int
```

---

## 🚀 Развертывание и мониторинг

### Docker Compose конфигурация

```yaml
version: '3.8'

services:
  # Temporal Server
  temporal:
    container_name: temporal
    depends_on:
      - postgresql
    environment:
      - DB=postgresql
      - DB_PORT=5432
      - POSTGRES_USER=temporal
      - POSTGRES_PWD=temporal
      - POSTGRES_SEEDS=postgresql
    image: temporalio/auto-setup:1.22.0
    ports:
      - 7233:7233
      - 8080:8080
    labels:
      kompose.volume.type: configMap
    volumes:
      - ./dynamicconfig:/etc/temporal/config/dynamicconfig

  # База данных
  postgresql:
    container_name: temporal-postgresql
    environment:
      POSTGRES_PASSWORD: temporal
      POSTGRES_USER: temporal
    image: postgres:13
    ports:
      - 5432:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data

  # API сервер
  api:
    build: .
    container_name: learning-api
    depends_on:
      - temporal
      - postgresql
    environment:
      - LLM_MODEL=openai/gpt-4o
      - LLM_KEY=${OPENAI_API_KEY}
      - TEMPORAL_HOST=temporal:7233
      - DATABASE_URL=postgresql://temporal:temporal@postgresql:5432/learning_db
    ports:
      - 8000:8000
    volumes:
      - .:/app
    command: uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

  # Worker
  worker:
    build: .
    container_name: learning-worker
    depends_on:
      - temporal
      - postgresql
    environment:
      - LLM_MODEL=openai/gpt-4o  
      - LLM_KEY=${OPENAI_API_KEY}
      - TEMPORAL_HOST=temporal:7233
    volumes:
      - .:/app
    command: python scripts/run_worker.py

  # Frontend
  frontend:
    build: ./frontend
    container_name: learning-frontend
    ports:
      - 3000:3000
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app
      - /app/node_modules

  # Redis для кэширования
  redis:
    image: redis:7-alpine
    container_name: learning-redis
    ports:
      - 6379:6379

volumes:
  postgres_data:
```

### Мониторинг и логирование

```python
import logging
from temporalio import activity
import structlog

# Настройка структурированного логирования
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

@activity.defn
async def generate_lesson_with_monitoring(lesson_data: dict) -> dict:
    """Activity с мониторингом производительности"""
    
    start_time = time.time()
    lesson_topic = lesson_data.get('topic', 'unknown')
    
    logger.info(
        "lesson_generation_started",
        topic=lesson_topic,
        user_level=lesson_data.get('user_level'),
        workflow_id=activity.info().workflow_id
    )
    
    try:
        # Генерация урока
        result = await actual_lesson_generation(lesson_data)
        
        duration = time.time() - start_time
        
        logger.info(
            "lesson_generation_completed",
            topic=lesson_topic,
            duration_seconds=duration,
            content_length=len(result.get('content', '')),
            workflow_id=activity.info().workflow_id
        )
        
        # Метрики для мониторинга
        await record_metrics({
            'lesson_generation_duration': duration,
            'content_length': len(result.get('content', '')),
            'topic': lesson_topic
        })
        
        return result
        
    except Exception as e:
        logger.error(
            "lesson_generation_failed",
            topic=lesson_topic,
            error=str(e),
            workflow_id=activity.info().workflow_id
        )
        raise
```

### Метрики для мониторинга

```python
from prometheus_client import Counter, Histogram, Gauge

# Метрики производительности
LESSON_GENERATION_DURATION = Histogram(
    'lesson_generation_duration_seconds',
    'Time spent generating lesson content',
    ['topic_category', 'user_level']
)

COURSE_CREATION_COUNTER = Counter(
    'courses_created_total',
    'Total number of courses created',
    ['topic_category']
)

ACTIVE_WORKFLOWS = Gauge(
    'active_learning_workflows',
    'Number of active learning workflows'
)

LLM_API_CALLS = Counter(
    'llm_api_calls_total', 
    'Total LLM API calls',
    ['model', 'operation']
)

# Использование в коде
@activity.defn  
async def generate_content_with_metrics(request: dict):
    with LESSON_GENERATION_DURATION.labels(
        topic_category=request['category'],
        user_level=request['level']
    ).time():
        
        LLM_API_CALLS.labels(
            model='gpt-4',
            operation='lesson_generation'
        ).inc()
        
        result = await generate_content(request)
        return result
```

---

Этот технический документ предоставляет детальное понимание того, как адаптировать архитектуру Temporal AI Agent для создания системы генерации обучающих материалов. Основные преимущества такого подхода:

1. **Надежность**: Temporal обеспечивает отказоустойчивость и восстановление после сбоев
2. **Масштабируемость**: Легко добавлять новые типы контента и инструменты
3. **Наблюдаемость**: Полное отслеживание процесса генерации контента
4. **Гибкость**: Возможность адаптации под разные типы обучающих материалов