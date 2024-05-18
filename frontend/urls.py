# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.main.as_view(), name='home'),
    path('check-symptoms/',views.checkSymptoms.as_view(), name='check-symptoms'),
    path('about-us/',views.aboutUs.as_view(), name='about-us'),
    path('users-data/',views.userListing.as_view(), name='users-data'),
]
