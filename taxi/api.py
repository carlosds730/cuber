from util.api import BasicResourceNoAuth
from taxi.models import Car


class CarResource(BasicResourceNoAuth):
    class Meta(BasicResourceNoAuth.Meta):
        queryset = Car.objects.all()
        resource_name = Car.RESOURCE_NAME
