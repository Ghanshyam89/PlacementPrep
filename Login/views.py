from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm
# Create your views here.

def login(request):
    form = LoginForm(request.POST)
    return render(request, 'login.html', {'form':form})