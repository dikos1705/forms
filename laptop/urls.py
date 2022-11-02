from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='laptop'),
    path('lenovo/', lenovo), #127.0.0.1:8080/phone/2/

]