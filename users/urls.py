from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView

app_name = 'users'


urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="register"),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name="blacklist"),
]

