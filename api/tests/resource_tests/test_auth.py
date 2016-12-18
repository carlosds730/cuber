from api.tests import APIAllowedMethodsTestsMixin, BasicAPITest
from account.api import SessionResource


class SessionResourceAllowedMethods(APIAllowedMethodsTestsMixin):
    RESOURCE_LIST_URI = '/api/v1/sessions/'

    def test_base(self):
        self.LIST_EXPECTED_RESPONSES = {
            'get': 405,
            'put': 405,
            'delete': 405
        }

        self.DETAIL_EXPECTED_RESPONSES = {
            'get': 405,
            'put': 405,
            'post': 405,
            'delete': 405
        }

        self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES = self.DETAIL_EXPECTED_RESPONSES

        self.AUTHENTICATED_LIST_EXPECTED_RESPONSES = self.LIST_EXPECTED_RESPONSES

        # self.run_base_tests()


class SessionResourceTest(BasicAPITest):
    RESOURCE_LIST_URI = '/api/v1/sessions/'

    def test_incorrect_password(self):
        resp = self.api_client.post(self.RESOURCE_LIST_URI, data={
            'username': self.DEFAULT_USER_NAME,
            'password': "{0} fake-pass".format(self.DEFAULT_USER_PASS)
        })

        self.assertHttpUnauthorized(resp)

        # We didn't send any cookies in the response
        self.assertEqual(len(resp.cookies), 0)

        # There is no csrftoken set in the test client
        self.assertNotIn('csrftoken', self.api_client.client.cookies)

    def test_successful_post(self):
        resp = self.api_client.post(self.RESOURCE_LIST_URI, data={
            'username': self.DEFAULT_USER_NAME,
            'password': self.DEFAULT_USER_PASS
        })

        self.assertHttpCreated(resp)

        cookie = resp.cookies

        self.assertIn('csrftoken', cookie)
        self.assertIn('sessionid', cookie)
