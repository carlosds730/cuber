import datetime
from api.tests import BasicAPITest, APIAllowedMethodsTestsMixin
from travels.models import TravelRequest
from taxi.models import Car

class TravelRequestAllowedMethods(APIAllowedMethodsTestsMixin):
    RESOURCE_LIST_URI = TravelRequest.resource_list_uri()

    def setUp(self):
        super(TravelRequestAllowedMethods, self).setUp()

        # Create a car
        new_car = Car(brand='Chevrolet', year=2013)
        # save it
        new_car.save()

        # new_driver =
        #
        # self.OBJECT_ID = new_car.id

    def test_base(self):
        # If the client is not logged in, he/she can't see any travel request
        self.DETAIL_EXPECTED_RESPONSES.update({
            'get': 401,
        })
        # # but no one can edit it
        # self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES.update({
        #     'get': 200,
        #     'put': 405,
        # })

        self.run_base_tests()
