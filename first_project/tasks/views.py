from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Welcome to the task page")

def all_task(request):
    return HttpResponse("Welcome to all tasks")