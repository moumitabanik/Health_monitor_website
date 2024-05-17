# views.py
from django.shortcuts import render
from django.views.generic.base import View

class main(View):
  def get(self, request, *args, **kwargs):
        return render(request, "main.html")  
