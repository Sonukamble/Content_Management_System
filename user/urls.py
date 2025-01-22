from django.urls import path
from .views import RegisterAuthor, LoginAPIView

urlpatterns = [
    path('auth/register/', RegisterAuthor.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
]
