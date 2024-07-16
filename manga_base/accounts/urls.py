from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns = [
  path('register', views.register, name='register'),
  path('my-login', views.my_login, name="my-login"),
  path('user-logout', views.user_logout, name='user-logout')
]