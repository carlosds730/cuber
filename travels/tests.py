from django.test import TestCase
from .models import Travel, TravelRequest
from taxi.models import Car, Driver
from tests import BasicTest
from taxi.tests import TaxiTestMixin
import datetime


# Create your tests here.
class TravelTestMixin(BasicTest):
    @staticmethod
    def create_travel():
        car = TaxiTestMixin.create_car()
        driver = TaxiTestMixin.create_driver()

    @staticmethod
    def create_travel_request(client=None):
        if not client:
            client = TravelTestMixin.create_user()
        return TravelRequest.objects.create(
            when=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-5))), duration=7, client=client)
