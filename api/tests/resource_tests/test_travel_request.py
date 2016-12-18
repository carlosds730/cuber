import datetime
from api.tests import BasicAPITest, APIAllowedMethodsTestsMixin
from travels.tests import TravelTestMixin
from travels.models import TravelRequest
from taxi.models import Car


class TravelRequestAllowedMethods(APIAllowedMethodsTestsMixin, TravelTestMixin):
    RESOURCE_LIST_URI = TravelRequest.resource_list_uri()

    def setUp(self):
        super(TravelRequestAllowedMethods, self).setUp()

        new_travel_request = TravelTestMixin.create_travel_request(self.profile)

        self.OBJECT_ID = new_travel_request.id

    def test_base(self):
        # If the client is not logged in, he/she can't see any travel request
        self.DETAIL_EXPECTED_RESPONSES.update({
            'get': 401,
            'put': 401
        })

        new_user = self.create_user()

        self.run_base_tests(new_user)
