# urls.py
from django.urls import path
from .views import health_chatbot_api, UserHealthDataList

urlpatterns = [
    path('health-chatbot/', health_chatbot_api, name='health_chatbot_api'),
    path('user-health-data/', UserHealthDataList.as_view(), name='user-health-data-list'),
]
