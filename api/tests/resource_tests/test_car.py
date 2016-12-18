from api.tests import BasicAPITest
from taxi.models import Car


class CarTest(BasicAPITest):
    RESOURCE_LIST_URI = Car.resource_list_uri()

    # Authentication tests for the resource
    def test_get_list_unauthenticated(self):
        self.assertHttpOK(self.api_client.get(self.RESOURCE_LIST_URI, format='json'))

    def test_get_list_authenticated(self):
        self.set_credentials(self.profile)
        self.assertHttpOK(self.api_client.get(self.RESOURCE_LIST_URI, format='json'))
