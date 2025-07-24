"""
URL configuration for aikademiya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

def api_root(request):
    """API Root - показывает доступные endpoints"""
    return JsonResponse({
        'message': 'AiKademiya API',
        'version': '1.0.0',
        'endpoints': {
            'auth': '/api/v1/auth/',
            'courses': '/api/v1/courses/',
            'quizzes': '/api/v1/quizzes/',
            'admin': '/admin/',
            'docs': '/api/schema/swagger-ui/',
        }
    })

def home_redirect(request):
    """Корневой маршрут - информация о том, что это API сервер"""
    return JsonResponse({
        'message': 'AiKademiya API Server',
        'version': '1.0.0',
        'info': 'This is the API server. Frontend is available at http://localhost:5173',
        'frontend_url': 'http://localhost:5173',
        'api_docs': 'http://localhost:8000/api/schema/swagger-ui/',
        'endpoints': {
            'api_root': '/api/',
            'auth': '/api/v1/auth/',
            'courses': '/api/v1/courses/',
            'quizzes': '/api/v1/quizzes/',
            'admin': '/admin/',
            'docs': '/api/schema/swagger-ui/',
        }
    })

urlpatterns = [
    path('', home_redirect, name='home'),  # Корневой маршрут
    path("admin/", admin.site.urls),
    path('api/', api_root, name='api-root'),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API v1 endpoints
    path("api/v1/auth/", include("users.api_urls")),
    path("api/v1/courses/", include("courses.api_urls")),
    path("api/v1/quizzes/", include("quizzes.api_urls")),
    
    # Legacy URLs (keep for backward compatibility)
    path("api/", include("courses.urls", namespace="courses")),
    path("quizzes/", include("quizzes.urls", namespace="quizzes")),
    path("progress/", include("progress.urls", namespace="progress")),
    path("generation/", include("generation.urls", namespace="generation")),
    path("billing/", include("billing.urls", namespace="billing")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("adminpanel/", include("adminpanel.urls", namespace="adminpanel")),
]
