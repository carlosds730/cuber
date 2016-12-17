import datetime
from api.tests import BasicAPITest


class Car(BasicAPITest):
    def test_get_list_unauthenticated(self):
        self.assertHttpOK(self.api_client.get('/api/v1/car/', format='json'))

    def test_get_list_authenticated(self):
        self.set_credentials(self.profile)
        self.assertHttpOK(self.api_client.get('/api/v1/car/', format='json'))

