from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
  return render(request, 'homepage.html')

def kitchen(request):
  return HttpResponse(request.body)

def bath(request):
  if request.session.has_key("session_token"):
    del request.session["session_token"]
  return render(request, 'bathroom.html')

def bed(request):
  return HttpResponse("THIS IS MY BEDROOM!!!!")

def guest(request):
  return HttpResponse("THIS IS MY GUESTROOM!!!!")

def office(request):
  return HttpResponse("THIS IS MY OFFICE!!!!")
