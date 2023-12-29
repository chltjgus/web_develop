from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to account!</h1>")

def about(request):
    return HttpResponse("About page")

def homePage(request):
    return HttpResponse("<h1>Hello World!!<h1>")

