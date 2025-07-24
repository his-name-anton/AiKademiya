from rest_framework import serializers
from .models import Course, Module, Chapter, CourseCategory
from users.serializers import UserProfileSerializer


class CourseCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий курсов"""
    class Meta:
        model = CourseCategory
        fields = ['id', 'name', 'created_at']


class ChapterSerializer(serializers.ModelSerializer):
    """Сериализатор для глав курса"""
    class Meta:
        model = Chapter
        fields = [
            'id', 'title', 'content', 'index', 'summary',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ChapterListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка глав (без полного контента)"""
    class Meta:
        model = Chapter
        fields = [
            'id', 'title', 'index', 'summary',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модулей курса"""
    chapters = ChapterListSerializer(many=True, read_only=True)
    chapters_count = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = [
            'id', 'title', 'short_description', 'index',
            'chapters', 'chapters_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_chapters_count(self, obj):
        return obj.chapters.count()


class ModuleListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка модулей (без глав)"""
    chapters_count = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = [
            'id', 'title', 'short_description', 'index',
            'chapters_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_chapters_count(self, obj):
        return obj.chapters.count()


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""
    created_by = UserProfileSerializer(read_only=True)
    category = CourseCategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    modules = ModuleListSerializer(many=True, read_only=True)
    modules_count = serializers.SerializerMethodField()
    total_chapters = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'level', 'goal', 'language',
            'is_public', 'created_by', 'category', 'category_id',
            'modules', 'modules_count', 'total_chapters',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_total_chapters(self, obj):
        return sum(module.chapters.count() for module in obj.modules.all())

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class CourseListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка курсов (краткая информация)"""
    created_by = serializers.CharField(source='created_by.email', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    modules_count = serializers.SerializerMethodField()
    total_chapters = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'level', 'language',
            'is_public', 'created_by', 'category',
            'modules_count', 'total_chapters', 'created_at'
        ]

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_total_chapters(self, obj):
        return sum(module.chapters.count() for module in obj.modules.all())


class CourseDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о курсе"""
    created_by = UserProfileSerializer(read_only=True)
    category = CourseCategorySerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    modules_count = serializers.SerializerMethodField()
    total_chapters = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'level', 'goal', 'language',
            'is_public', 'created_by', 'category', 'modules',
            'modules_count', 'total_chapters', 'created_at', 'updated_at'
        ]

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_total_chapters(self, obj):
        return sum(module.chapters.count() for module in obj.modules.all())


class CourseGenerationSerializer(serializers.Serializer):
    """Сериализатор для генерации курса"""
    topic = serializers.CharField(max_length=500)
    level = serializers.ChoiceField(
        choices=Course.LEVEL_CHOICES,
        default='beginner'
    )
    goal = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    language = serializers.CharField(max_length=10, default='ru')
    category_id = serializers.IntegerField(required=False, allow_null=True)

    def validate_topic(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                'Тема курса должна содержать минимум 5 символов'
            )
        return value.strip()

    def validate_category_id(self, value):
        if value is not None:
            try:
                CourseCategory.objects.get(id=value)
            except CourseCategory.DoesNotExist:
                raise serializers.ValidationError(
                    'Категория с указанным ID не существует'
                )
        return value