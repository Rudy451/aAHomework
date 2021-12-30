from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
  return HttpResponse("THIS IS MY HOUSE!!!!")

def kitchen(request):
  return HttpResponse(request.body)

def bath(request):
  return HttpResponse("THIS IS MY BATHROOM!!!!")

def bed(request):
  return HttpResponse("THIS IS MY BEDROOM!!!!")

def guest(request):
  return HttpResponse("THIS IS MY GUESTROOM!!!!")

def office(request):
  return HttpResponse("THIS IS MY OFFICE!!!!")
