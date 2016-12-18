from django.test import TestCase
from .models import Travel, TravelRequest
from taxi.models import Car, Driver
from tests import BasicTest


# Create your tests here.
class TravelTestMixin(BasicTest):

    def create_travel(self):
        pass
