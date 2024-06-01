from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from read.models import Manga


def home(request):

  manga = Manga.objects.all()

  context = {
    'manga': manga
  }

  return render(request, "main/index.html", context)