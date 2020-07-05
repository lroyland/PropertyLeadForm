from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Testing basic Http Response in form views.py")
# Create your views here.
