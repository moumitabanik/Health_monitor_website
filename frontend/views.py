# views.py
from django.shortcuts import render
from django.views.generic.base import View

class main(View):
  def get(self, request, *args, **kwargs):
        return render(request, "home.html")  
  
class checkSymptoms(View):
  def get(self, request, *args, **kwargs):
        return render(request, "check_symptoms.html")  
  
class aboutUs(View):
  def get(self, request, *args, **kwargs):
        return render(request, "about_us.html")  

class userListing(View):
  def get(self, request, *args, **kwargs):
        return render(request, "user_listing.html")  
