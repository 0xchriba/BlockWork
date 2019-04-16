from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> HomePage </h1>')

def job(request):
    return HttpResponse('<h1> Job </h1>')

# Create your views here.
