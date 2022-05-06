import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import JsonResponse

def register(request):
  if request.method == "POST":
    context = {
    first_name = request.POST["first_name"],
    last_name = request.POST["last_name"],
    email = request.POST["email"],
    password = request.POST["password"]
    }
  return render(request, 'register.html')

def login(request):
  return render(request, 'login.html')

def index(request):
  return render(request, 'index.html')

def welcome(request):
  context = {
    'first_name':
  }
  return render(request, 'welcome.html', context)