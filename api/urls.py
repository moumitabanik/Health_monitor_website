# urls.py
from django.urls import path
from .views import health_chatbot_api

urlpatterns = [
    path('health-chatbot/', health_chatbot_api, name='health_chatbot_api'),
]
