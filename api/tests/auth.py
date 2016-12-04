import datetime
from . import BasicAPITest


class EntryResourceTest(BasicAPITest):
    def test_get_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/car/', format='json'))
