
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,Http404
from.models import * 
from.forms import *
from django.views import View
from django.shortcuts import redirect
# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, 'car/index.html',{'cars':cars,'title':'Машины',})


class CarListView(View):
    tempplate_name = 'car/index.html'
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'car/index.html',{'cars':cars,'title':'Машины',})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        car.delete()                     # delete the cat.
        return redirect('/car/')             # Finally, redirect to the homepage.

    return render(request, 'car/delete.html',{'object':car})
class CarUpdateView(View):

    queryset = []
    swiped_movies=[]

    def get(self, request):

        # Get the room id from the request
        car_id = request.GET.get('id')
        
        if car_id: 
            queryset = Car.objects.filter(id=car_id)

        else: 
            queryset = Car.objects.all()
        
        print(queryset)
        print("BRUHHHH")
        
        form = AddPostForm
        
        return render(request,'car/edit.html',{'details':queryset, 'form':form})
    def post(request, pk):
        form = AddPostForm(request.POST,request.FILES)
        submitted = False
        if request.method == "POST":
            if form.is_valid():
                print("Getting here!!!!!!!")
                form.save(commit=False)
                
        else:
            form = AddPostForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request,'car/edit.html',{'details':queryset, 'form':form,'submitted':submitted})
#     
def add(request):
    if  request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Car.objects.create(**form.cleaned_data)
            except Exception:
                form.add_error(None,"Ошибка добавление Поста")
            return redirect('/car/')
    else:
        form = AddPostForm()
    return render(request,'car/add.html',{'form':form})



def categories(request,carid):
    if carid >10 :
        raise Http404()
    return HttpResponse(f'<h1>categories:<h1> <p>{carid}</p>')

def carmodel(request,carmodel):
    carmodels = [ 'Mercedes', 'Honda', 'BMW', 'Huyindai','Audi']
    if carmodel not in carmodels:
        raise Http404()
    print(request.GET)
    if request.GET:
        if carmodel =="Audi" and 'A8' in request.GET:
            return HttpResponse(f'<h1>models:<h1> <p>Машина марка {carmodel}</p> <p>Машина модели А8</p> '  )
    

    return HttpResponse(f'<h1>models:<h1> <p>Машина модели {carmodel}</p>')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не Найдена</h1> <p>ошибка 404</p>')