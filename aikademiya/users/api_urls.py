from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    ChangePasswordView,
    verify_token
)

urlpatterns = [
    # Authentication
    path('register/', UserRegistrationView.as_view(), name='api_user_register'),
    path('login/', UserLoginView.as_view(), name='api_user_login'),
    path('logout/', UserLogoutView.as_view(), name='api_user_logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
    path('token/verify/', verify_token, name='api_token_verify'),
    
    # Profile management
    path('profile/', UserProfileView.as_view(), name='api_user_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='api_change_password'),
]