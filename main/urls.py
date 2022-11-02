
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('<pk>/', get_product, name = '')
    # path('',include('main.urls')), #127.0.0.1:8080/
]




