from rest_framework import serializers
import json
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов теста"""
    options_list = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id', 'text', 'options_list', 'correct_answer',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_options_list(self, obj):
        """Преобразует строку опций в список"""
        try:
            return json.loads(obj.options) if obj.options else []
        except (json.JSONDecodeError, TypeError):
            # Если options хранятся как строка, разделяем по переносам
            return obj.options.split('\n') if obj.options else []


class QuestionCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления вопросов"""
    options_list = serializers.ListField(
        child=serializers.CharField(max_length=500),
        min_length=2,
        max_length=6,
        write_only=True
    )

    class Meta:
        model = Question
        fields = [
            'id', 'chapter', 'text', 'options_list', 'correct_answer',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_correct_answer(self, value):
        """Проверяем, что правильный ответ не пустой"""
        if not value or not value.strip():
            raise serializers.ValidationError(
                'Правильный ответ не может быть пустым'
            )
        return value.strip()

    def validate(self, attrs):
        """Проверяем, что правильный ответ есть среди вариантов"""
        options_list = attrs.get('options_list', [])
        correct_answer = attrs.get('correct_answer', '').strip()
        
        if correct_answer and correct_answer not in options_list:
            raise serializers.ValidationError(
                'Правильный ответ должен быть среди вариантов ответов'
            )
        
        return attrs

    def create(self, validated_data):
        options_list = validated_data.pop('options_list')
        validated_data['options'] = json.dumps(options_list, ensure_ascii=False)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'options_list' in validated_data:
            options_list = validated_data.pop('options_list')
            validated_data['options'] = json.dumps(options_list, ensure_ascii=False)
        return super().update(instance, validated_data)


class QuestionAnswerSerializer(serializers.Serializer):
    """Сериализатор для ответа на вопрос"""
    answer = serializers.CharField(max_length=500)

    def validate_answer(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError(
                'Ответ не может быть пустым'
            )
        return value.strip()


class QuizResultSerializer(serializers.Serializer):
    """Сериализатор для результатов теста"""
    question_id = serializers.IntegerField()
    user_answer = serializers.CharField(max_length=500)
    is_correct = serializers.BooleanField()
    correct_answer = serializers.CharField(max_length=500)


class ChapterQuizResultSerializer(serializers.Serializer):
    """Сериализатор для результатов теста по главе"""
    chapter_id = serializers.IntegerField()
    total_questions = serializers.IntegerField()
    correct_answers = serializers.IntegerField()
    score_percentage = serializers.FloatField()
    questions_results = QuizResultSerializer(many=True)
    passed = serializers.BooleanField()  # Прошел ли тест (например, >70%)