from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
# Create your views here.

def loginRegister(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            return HttpResponseRedirect('/', "user created")
    else:
        form = RegistrationForm()
    return render(request, 'loginRegister.html', {'form':form})