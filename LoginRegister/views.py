from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loginRegister(request):
    return render(request, 'loginRegister.html');