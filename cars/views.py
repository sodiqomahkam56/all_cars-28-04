from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CarForm
from .models import Car


def create_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        color = request.POST.get('color')
        price = request.POST.get('price')

        if brand and model and year and color and price:
            try:
                year = int(year)
                price = Decimal(price)
                Car.objects.create(
                    brand=brand,
                    model=model,
                    year=year,
                    color=color,
                    price=price
                )
                return redirect('cars-list')
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("FORM IS INCOMPLETE")

    return render(request, 'cars/create_car.html')




def get_cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'cars/cars_list.html', context)


def create_car_form(request):
    if request.method == 'POST':
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars-list')
        else:
            return render(request, 'cars/create_car_form.html',{'form':form})
    else:
        form=CarForm(request.POST)
    return render(request, 'cars/create_car_form.html',{'form':form})

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)


def car_update(request, id):
    car=Car.objects.get(id=id)
    if request.method=='POST':
        form=CarForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars-list')
        else:
            return HttpResponse("Form is not valid",status=400)
    else:
        form=CarForm(instance=car)
    return render(request,'cars/create_car_form.html',{'form':form})









