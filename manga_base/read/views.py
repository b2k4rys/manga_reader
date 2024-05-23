from django.shortcuts import render

# Create your views here.

def jjk(request):
  return render(request, 'read/index.html')