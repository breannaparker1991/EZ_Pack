from difflib import context_diff
import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import JsonResponse


def index(request):
    return render(request,'index.html')

def register(request):
  return render(request, 'register.html')

def create(request): 
  request.method = 'POST'
  first_name = request.POST["first_name"]
  last_name = request.POST["last_name"]
  email = request.POST["email"]
  password = request.POST["password"]
  return redirect('welcome.html')

def login(request):
  return render(request, 'login.html')

def welcome(request):
  # context = {
  #   'first_name': 
  # }
  return render(request, 'welcome.html', context)