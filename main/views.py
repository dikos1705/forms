from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    p = Products.objects.all()
    return render(request,'main/index.html', {'products': p,})   

def get_product(request,pk):
    p = Products.objects.get(pk=pk)

    return render(request,'main/product.html', {'p': p,})   