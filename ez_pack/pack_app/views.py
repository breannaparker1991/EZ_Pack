from django.shortcuts import render, redirect
from django.http import JsonResponse

def login(request):
  return render(request, 'index.html')
