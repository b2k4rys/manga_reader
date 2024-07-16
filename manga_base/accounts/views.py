from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import CreateUserForm, LoginForm
# Create your views here.
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def register(request):

  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('my-login')
    
  context = {'registerform': form}
  
  return render(request, 'accounts/register.html', context)




def my_login(request):
  form = LoginForm()

  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)

    if form.is_valid():

      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        auth.login(request, user)

        return redirect('/')
      
  context = {'loginform': form}
  return render(request, 'accounts/my-login.html', context)

def user_logout(request):

  auth.logout (request)
  return redirect('/')