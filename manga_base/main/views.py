from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from read.models import Categories

def home(request):
  categories = Categories.objects.all()

  context = {
    'title': 'Home',
    'categories': categories
  }
  return render(request, "main/index.html")