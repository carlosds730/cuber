from tests import BasicTest
from .models import Car, Driver
from util.utils import random_string, get_random_first_name, get_random_last_name, \
    get_random_id_number, get_random_license_number


class TaxiTestMixin(BasicTest):
    @staticmethod
    def create_car():
        return Car.objects.create(brand=random_string(['Chevrolet', 'Chevy', 'Mercedes']), year=2013)

    @staticmethod
    def create_driver():
        first_name = get_random_first_name()
        alias = "The {0}".format(first_name)

        return Driver.objects.create(first_name=first_name, last_name=get_random_last_name(), alias=alias,
                                     id_number=get_random_id_number(), license_number=get_random_license_number())

# Create your tests here.
