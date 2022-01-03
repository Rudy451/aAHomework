from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

import bcrypt
import random

from .forms import UserForm
from .models import MyUser

# Create your views here.
def formCheck(request):
  if request.session.has_key("session_token"):
    return render(request, 'homepage.html')
  else:
    user_form = UserForm()
    return render(request, 'signup.html', {'form': user_form})

def signup(request):
  form = UserForm(request.POST)
  if form.is_valid():
    form.cleaned_data
    user = MyUser()
    user.user_name = str(request.POST.get("user_name"))
    salt = bcrypt.gensalt()
    user.password = str(bcrypt.hashpw(b'f"{form["password"]}"', salt))
    user.session_token = True
    user.save()
    request.session["session_token"] = user.session_token
    request.session.save()
  return redirect('/')

def login(request):
  pass
