from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='phone'),
    # path('2/', index2), #127.0.0.1:8080/phone/2/

]