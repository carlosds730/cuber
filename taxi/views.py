from django.shortcuts import render
from taxi.models import Car


# Create your views here.
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'taxi/car.html', {'cars': cars})
