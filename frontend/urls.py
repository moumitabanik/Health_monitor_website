# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main.as_view(), name=''),
]
