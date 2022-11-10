from django.urls import path, include
from .views import RegistrationAPIView


urlpatterns = [
    path('login/', RegistrationAPIView.as_view()),
]