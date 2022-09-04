from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def quiz(request):
    return render(request, 'quiz.html')

    
