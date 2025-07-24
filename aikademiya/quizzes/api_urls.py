from django.urls import path
from .api_views import (
    ChapterQuestionsView,
    QuestionDetailView,
    AnswerQuestionView,
    ChapterQuizView,
    chapter_quiz_questions
)

urlpatterns = [
    # Questions for a specific chapter
    path('chapters/<int:chapter_id>/questions/', ChapterQuestionsView.as_view(), name='api_chapter_questions'),
    path('chapters/<int:chapter_id>/quiz/', chapter_quiz_questions, name='api_chapter_quiz_questions'),
    
    # Individual question management
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='api_question_detail'),
    
    # Quiz taking
    path('questions/<int:question_id>/answer/', AnswerQuestionView.as_view(), name='api_answer_question'),
    path('chapters/<int:chapter_id>/take-quiz/', ChapterQuizView.as_view(), name='api_chapter_take_quiz'),
]