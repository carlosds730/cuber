from api.tests import APIAllowedMethodsTestsMixin, BasicAPITest
from taxi.models import Car


class CarResourceAllowedMethods(APIAllowedMethodsTestsMixin):
    RESOURCE_LIST_URI = Car.resource_list_uri()

    def setUp(self):
        super(CarResourceAllowedMethods, self).setUp()

        # Create a car
        new_car = Car(brand='Chevrolet', year=2013)
        # save it
        new_car.save()

        self.OBJECT_ID = new_car.id

    def test_base(self):
        # We allow everyone to view all the cars
        # We do not allow anyone to POST a car
        self.LIST_EXPECTED_RESPONSES.update({
            'get': 200,
            'post': 405
        })
        # Everyone can see a car
        self.DETAIL_EXPECTED_RESPONSES.update({
            'get': 200,
        })
        # but no one can edit it
        self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES.update({
            'get': 200,
            'put': 405,
        })

        self.run_base_tests()


class CarResourceTest(BasicAPITest):
    RESOURCE_LIST_URI = Car.resource_list_uri()

