from django.urls import path

from . import views

urlpatterns = [
    path('quote/', views.quotes, name= 'Quote'),
]