from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.home, name='home'),
  path('my-profile', views.profile, name='profile'),
  path('my-profile/change-password', views.change_password, name='change-password')
]
