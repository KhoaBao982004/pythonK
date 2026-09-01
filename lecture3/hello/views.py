from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("Hello, World")

def khoa(request):
  return HttpResponse("Hello, Khoa!")


def david(request):
  return HttpResponse("Hello, David!!!!")


def greet(request, name):
  return HttpResponse("Hello, {name}!!!")