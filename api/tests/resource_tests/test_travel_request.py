import datetime
from api.tests import BasicAPITest
from travels.models import TravelRequest
from travels.api import TravelRequestResource


class TravelRequestTest(BasicAPITest):
    RESOURCE_LIST_URI = TravelRequest.resource_list_uri()

    # Authentication tests for the resource
    def test_get_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get(self.RESOURCE_LIST_URI, format='json'))

    # TODO
    def test_get_details_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get(self.RESOURCE_LIST_URI, format='json'))

    def test_get_list_authenticated(self):
        self.set_credentials(self.profile)
        self.assertHttpOK(self.api_client.get(self.RESOURCE_LIST_URI, format='json'))
