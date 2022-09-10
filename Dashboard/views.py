from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Questions


def main(request):
    if request.user.is_authenticated:
        que_list = Questions.objects.all()
        return render(request, 'main.html', 
                {'que_list': que_list})
        # return render(request, 'main.html') 
    # messages.info(request, 'Please login with your credentials to access this page!')
    return  redirect('login')
