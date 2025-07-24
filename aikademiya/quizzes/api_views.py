from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Question
from courses.models import Chapter
from .serializers import (
    QuestionSerializer, QuestionCreateUpdateSerializer, 
    QuestionAnswerSerializer, QuizResultSerializer,
    ChapterQuizResultSerializer
)


class ChapterQuestionsView(generics.ListCreateAPIView):
    """
    Список вопросов для главы курса
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        chapter = get_object_or_404(Chapter, id=chapter_id)
        
        # Проверяем доступ к главе через курс
        if not chapter.module.course.is_public and chapter.module.course.created_by != self.request.user and not self.request.user.is_staff:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("У вас нет доступа к этой главе")
        
        return Question.objects.filter(chapter=chapter)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionSerializer
        return QuestionCreateUpdateSerializer

    @extend_schema(
        summary="Список вопросов главы",
        description="Получение списка всех вопросов для конкретной главы курса"
    )
    def get(self, request, chapter_id, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Создать вопрос",
        description="Создание нового вопроса для главы (только владелец курса или админ)",
        request=QuestionCreateUpdateSerializer
    )
    def post(self, request, chapter_id, *args, **kwargs):
        chapter = get_object_or_404(Chapter, id=chapter_id)
        
        # Проверяем права на создание вопросов
        if chapter.module.course.created_by != request.user and not request.user.is_staff:
            return Response({
                'error': 'У вас нет прав на создание вопросов для этого курса'
            }, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chapter=chapter)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детальная информация о вопросе, обновление и удаление
    """
    queryset = Question.objects.select_related('chapter__module__course')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionSerializer
        return QuestionCreateUpdateSerializer

    def get_object(self):
        obj = super().get_object()
        
        # Проверяем права доступа
        if self.request.method == 'GET':
            if not obj.chapter.module.course.is_public and obj.chapter.module.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет доступа к этому вопросу")
        else:
            if obj.chapter.module.course.created_by != self.request.user and not self.request.user.is_staff:
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("У вас нет прав на изменение этого вопроса")
        
        return obj


class AnswerQuestionView(APIView):
    """
    Ответ на конкретный вопрос
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Ответить на вопрос",
        description="Отправка ответа на конкретный вопрос и получение результата",
        request=QuestionAnswerSerializer,
        responses={
            200: QuizResultSerializer,
            400: OpenApiResponse(description="Ошибки валидации"),
            404: OpenApiResponse(description="Вопрос не найден")
        }
    )
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        
        # Проверяем доступ к вопросу
        if not question.chapter.module.course.is_public and question.chapter.module.course.created_by != request.user and not request.user.is_staff:
            return Response({
                'error': 'У вас нет доступа к этому вопросу'
            }, status=status.HTTP_403_FORBIDDEN)
        
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():
            user_answer = serializer.validated_data['answer']
            is_correct = user_answer == question.correct_answer
            
            result_data = {
                'question_id': question.id,
                'user_answer': user_answer,
                'is_correct': is_correct,
                'correct_answer': question.correct_answer
            }
            
            result_serializer = QuizResultSerializer(data=result_data)
            if result_serializer.is_valid():
                return Response(result_serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterQuizView(APIView):
    """
    Прохождение теста по главе
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Пройти тест по главе",
        description="Отправка ответов на все вопросы главы и получение результатов",
        request={
            'type': 'object',
            'properties': {
                'answers': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'question_id': {'type': 'integer'},
                            'answer': {'type': 'string'}
                        }
                    }
                }
            }
        },
        responses={
            200: ChapterQuizResultSerializer,
            400: OpenApiResponse(description="Ошибки валидации"),
            404: OpenApiResponse(description="Глава не найдена")
        }
    )
    def post(self, request, chapter_id):
        chapter = get_object_or_404(Chapter, id=chapter_id)
        
        # Проверяем доступ к главе
        if not chapter.module.course.is_public and chapter.module.course.created_by != request.user and not request.user.is_staff:
            return Response({
                'error': 'У вас нет доступа к этой главе'
            }, status=status.HTTP_403_FORBIDDEN)
        
        answers = request.data.get('answers', [])
        if not answers:
            return Response({
                'error': 'Необходимо предоставить ответы'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Получаем все вопросы главы
        questions = Question.objects.filter(chapter=chapter)
        if not questions.exists():
            return Response({
                'error': 'В этой главе нет вопросов'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Создаем словарь вопросов для быстрого поиска
        questions_dict = {q.id: q for q in questions}
        
        # Проверяем ответы
        results = []
        correct_count = 0
        
        for answer_data in answers:
            question_id = answer_data.get('question_id')
            user_answer = answer_data.get('answer', '').strip()
            
            if question_id not in questions_dict:
                continue  # Пропускаем вопросы, не относящиеся к этой главе
            
            question = questions_dict[question_id]
            is_correct = user_answer == question.correct_answer
            
            if is_correct:
                correct_count += 1
            
            results.append({
                'question_id': question_id,
                'user_answer': user_answer,
                'is_correct': is_correct,
                'correct_answer': question.correct_answer
            })
        
        total_questions = len(questions)
        score_percentage = (correct_count / total_questions * 100) if total_questions > 0 else 0
        passed = score_percentage >= 70  # Порог прохождения 70%
        
        result_data = {
            'chapter_id': chapter_id,
            'total_questions': total_questions,
            'correct_answers': correct_count,
            'score_percentage': round(score_percentage, 2),
            'questions_results': results,
            'passed': passed
        }
        
        result_serializer = ChapterQuizResultSerializer(data=result_data)
        if result_serializer.is_valid():
            return Response(result_serializer.data, status=status.HTTP_200_OK)
        
        return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="Получить вопросы главы без правильных ответов",
    description="Получение списка вопросов главы для прохождения теста (без правильных ответов)",
    responses={
        200: OpenApiResponse(description="Список вопросов для теста"),
        403: OpenApiResponse(description="Нет доступа"),
        404: OpenApiResponse(description="Глава не найдена")
    }
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def chapter_quiz_questions(request, chapter_id):
    """
    Получение вопросов для прохождения теста по главе
    (без правильных ответов)
    """
    chapter = get_object_or_404(Chapter, id=chapter_id)
    
    # Проверяем доступ к главе
    if not chapter.module.course.is_public and chapter.module.course.created_by != request.user and not request.user.is_staff:
        return Response({
            'error': 'У вас нет доступа к этой главе'
        }, status=status.HTTP_403_FORBIDDEN)
    
    questions = Question.objects.filter(chapter=chapter)
    
    # Сериализуем вопросы без правильных ответов
    questions_data = []
    for question in questions:
        question_serializer = QuestionSerializer(question)
        question_data = question_serializer.data
        # Убираем правильный ответ для теста
        question_data.pop('correct_answer', None)
        questions_data.append(question_data)
    
    return Response({
        'chapter_id': chapter_id,
        'chapter_title': chapter.title,
        'questions': questions_data,
        'total_questions': len(questions_data)
    }, status=status.HTTP_200_OK)