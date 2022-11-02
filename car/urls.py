


from django.urls import path,include
from .views import *

urlpatterns = [
    path('', CarListView.as_view(),name= 'car'),
    path('add/', add,name= 'add'),#127.0.0.1:8080/car/add/
    path('<pk>/delete',car_delete ,), #127.0.0.1:8080/car/int
    path('<pk>/update',CarUpdateView.as_view() ,), #127.0.0.1:8080/car/int
    # path('<str:carmodel>/', carmodel), #127.0.0.1:8080/car/int
    
]
#str любая не пустая строка без /
#int любое положительное число 
#slug слаг, то есть латиница Ascii таблица, дефиса и подчеркивания
# uuid цифры малые латинские символы AScii дефис
# path любая не пустая строка включая символ /

# <>