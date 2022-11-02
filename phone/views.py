from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'phone/index.html')

def index2(request):
    return HttpResponse("2 айфон")