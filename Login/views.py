from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate

def login(request):
    # form = LoginForm(request.POST  or None)
    # if request.method == "POST" and form.is_valid():
    #     uname = form.cleaned_data['username']
    #     upassword = form.cleaned_data['password']

    #     user = authenticate(username = uname, password = upassword)
    #     if user is not None:
    #         return HttpResponseRedirect('/main', "Successfully Signed in!")
    #     else:
    #         return HttpResponseRedirect('/', "Please Check your credentials!")
    # else:
    #     form = LoginForm()
    return render(request, 'login.html')
# , {'form':form}