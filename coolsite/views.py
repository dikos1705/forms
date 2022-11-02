from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404
from car.models import *
from phone.models import *
from laptop.models import *

def index(request):
    cars=    Car.objects.all()
    context = {'cars': cars}
    return render(request, 'main/index.html',context)



