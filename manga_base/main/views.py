from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

from read.models import Manga


def home(request):

  manga = Manga.objects.all()

  context = {
    'manga': manga
  }

  return render(request, "main/index.html", context)

def profile(request):

  username = request.user.username
  
  context = {
    'user_name': username
  }

  return render(request, 'main/profile.html', context)

def change_password(request):

  if request.method == 'POST':
    
    form = PasswordChangeForm(request.user, request.POST)

    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Your password was successfully updated!')
      return redirect('change_password')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form = PasswordChangeForm(request.user)

  context = {
    'form': form
  }

  return render(request, 'accounts/change_password.html', context)