from django.urls import path
from . import views

app_name = 'read'

urlpatterns = [
  path('<slug:manga_slug>/', views.read, name='read_manga')
]
