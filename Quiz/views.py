from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def quiz(request):
    if request.user.is_authenticated:
        return render(request, 'quiz.html') 
    return  redirect('login')
    