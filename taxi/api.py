from tastypie.resources import ModelResource
from tastypie.authentication import MultiAuthentication, BasicAuthentication, ApiKeyAuthentication
from taxi.models import Car


class CarResource(ModelResource):
    class Meta:
        queryset = Car.objects.all()
        resource_name = Car.RESOURCE_NAME
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
