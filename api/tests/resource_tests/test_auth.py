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
        resp = self.login(username=self.DEFAULT_USER_NAME, password="{0} fake-pass".format(self.DEFAULT_USER_PASS),
                          expected_result=401)

        # We didn't send any cookies in the response
        self.assertEqual(len(resp.cookies), 0)

        # There is no csrftoken set in the test client
        self.assertNotIn('csrftoken', self.api_client.client.cookies)

    def test_incorrect_user(self):
        resp = self.login(username="{0} fake-user".format(self.DEFAULT_USER_NAME),
                          password=self.DEFAULT_USER_PASS, expected_result=401)

        # We didn't send any cookies in the response
        self.assertEqual(len(resp.cookies), 0)

        # There is no csrftoken set in the test client
        self.assertNotIn('csrftoken', self.api_client.client.cookies)

    def test_successful_post(self):
        resp = self.login()

        cookie = resp.cookies

        # Verify we sent cookies in the response
        self.assertIn('csrftoken', cookie)
        self.assertIn('sessionid', cookie)

        # Verify that cookies are now set in the test client
        self.assertEqual(cookie['csrftoken'], self.api_client.client.cookies['csrftoken'])
        self.assertEqual(cookie['sessionid'], self.api_client.client.cookies['sessionid'])
