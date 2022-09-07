from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html') 
    # messages.info(request, 'Please login with your credentials to access this page!')
    return  redirect('login')
