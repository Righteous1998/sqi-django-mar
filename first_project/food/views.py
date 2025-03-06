from django.shortcuts import render, HttpResponse

# Create your views here.

def menu(request):
    return HttpResponse("Welcome to food menu")

def contact(request):
    return HttpResponse("Contact us here")