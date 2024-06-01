from django.shortcuts import render

# Create your views here.
from read.models import Manga

def read(request, manga_slug):
  manga = Manga.objects.get(slug=manga_slug)

  chapters = []
  for i in range(int(manga.number_of_chapters)):
    chapters.append(i)
  context = {
    'manga': manga,
    'chapters': chapters
  }
  
  return render(request, 'read/index.html', context)