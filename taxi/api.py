from tastypie.resources import ModelResource
from taxi.models import Car

class CarResource(ModelResource):
    class Meta:
        queryset = Car.objects.all()
        resource_name = 'car'