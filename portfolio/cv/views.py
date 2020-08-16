from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("this is testing page")

def home(request):
    return HttpResponse("this is testing home page")