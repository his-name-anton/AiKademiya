from django.urls import path
from .api_views import (
    CourseCategoryListView,
    CourseListCreateView,
    CourseDetailView,
    ModuleDetailView,
    ChapterDetailView,
    CourseGenerationView,
    course_generation_status,
    confirm_course_generation,
    generate_next_chapter
)

urlpatterns = [
    # Categories
    path('categories/', CourseCategoryListView.as_view(), name='api_course_categories'),
    
    # Courses
    path('', CourseListCreateView.as_view(), name='api_courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='api_course_detail'),
    
    # Modules
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name='api_module_detail'),
    
    # Chapters
    path('chapters/<int:pk>/', ChapterDetailView.as_view(), name='api_chapter_detail'),
    
    # AI Course Generation
    path('generate/', CourseGenerationView.as_view(), name='api_course_generate'),
    path('generate/<str:workflow_id>/status/', course_generation_status, name='api_course_generation_status'),
    path('generate/<str:workflow_id>/confirm/', confirm_course_generation, name='api_course_generation_confirm'),
    path('generate/<str:workflow_id>/next-chapter/', generate_next_chapter, name='api_course_generation_next_chapter'),
]