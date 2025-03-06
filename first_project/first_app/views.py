from django.shortcuts import render, HttpResponse

# Create your views here.
def home(Request):
    return HttpResponse("Welcome to my first django app")