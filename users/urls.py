from django.urls import path
from .views import CustomUserCreate

app_name = 'users'


urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="register"),
    # path('auth/login/', LoginView.as_view(), name="auth-login"),
]

