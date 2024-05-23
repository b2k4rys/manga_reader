from django.urls import path
from . import views

app_name = 'read'

urlpatterns = [
  path('jujutsu-kaisen', views.jjk, name='jjk')
]
