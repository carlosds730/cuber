from tests import BasicTest
from .models import Car, Driver
from util.utils import get_random_user_name, random_string


class TaxiTestMixin(BasicTest):
    def create_car(self):
        # Create a car
        return Car.objects.create(brand=random_string(['Chevrolet', 'Chevy', 'Mercedes']), year=2013)

    def create_driver(self):
        return Driver.objects.create(first_name=get_random_user_name())

# Create your tests here.
