from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to my app!</h1>")

def about(request):
    return HttpResponse("About page")

def homeV1(request):
    return HttpResponse("<h2>This page is V1<h2>")

