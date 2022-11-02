from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return HttpResponse("Ноутбук ACER")

def lenovo(request):
    return HttpResponse("Ноутбук Lenovo")