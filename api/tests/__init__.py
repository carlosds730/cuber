from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from tests import BasicTest


class BasicAPITest(ResourceTestCaseMixin, BasicTest):
    RESOURCE_LIST_URI = None

    def setUp(self):
        super(BasicAPITest, self).setUp()

        # Create a profile
        self.profile = BasicAPITest.create_user(user_name='test_user', password='pass', email='test_user@cuber.com')

    def tearDown(self):
        super(BasicAPITest, self).tearDown()

        # Clear the credentials
        self.clear_credentials()

    def get_credentials(self, profile=None):
        if not profile:
            profile = self.profile
        return self.create_apikey(username=profile.user.username, api_key=profile.get_my_key())

    def set_credentials(self, profile=None):
        self.api_client.client.defaults['HTTP_AUTHORIZATION'] = self.get_credentials(profile)

    def clear_credentials(self):
        if 'HTTP_AUTHORIZATION' in self.client.defaults:
            del self.client.defaults['HTTP_AUTHORIZATION']
        if 'HTTP_AUTHORIZATION' in self.api_client.client.defaults:
            del self.api_client.client.defaults['HTTP_AUTHORIZATION']


class APIAllowedMethodsTestsMixin(BasicAPITest):
    LIST_EXPECTED_RESPONSES = {'get': 401, 'post': 401, 'put': 405, 'delete': 405}
    DETAIL_EXPECTED_RESPONSES = {'get': 401, 'post': 405, 'put': 405, 'delete': 405}

    AUTHENTICATED_LIST_EXPECTED_RESPONSES = {'get': 200, 'put': 405, 'delete': 405}
    AUTHENTICATED_DETAIL_EXPECTED_RESPONSES = {'get': 401, 'post': 405, 'put': 401, 'delete': 405}

    OBJECT_ID = 1
    RESOURCE_LIST_URI = None

    def setUp(self):
        super(APIAllowedMethodsTestsMixin, self).setUp()
        self._set_defaults_responses()

    def _set_defaults_responses(self):
        self.LIST_EXPECTED_RESPONSES = {'get': 401, 'post': 401, 'put': 405, 'delete': 405}
        self.DETAIL_EXPECTED_RESPONSES = {'get': 401, 'post': 405, 'put': 405, 'delete': 405}

        self.AUTHENTICATED_LIST_EXPECTED_RESPONSES = {'get': 200, 'put': 405, 'delete': 405}
        self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES = {'get': 401, 'post': 405, 'put': 401, 'delete': 405}

    def _test_list_responses_unauthenticated(self):
        for verb in self.LIST_EXPECTED_RESPONSES:
            print(verb, self.LIST_EXPECTED_RESPONSES[verb])
            self.assertEqual(getattr(self.api_client, verb)(self.RESOURCE_LIST_URI, format='json').status_code,
                             self.LIST_EXPECTED_RESPONSES[verb])

    def _test_list_responses_authenticated(self, profile):
        self.set_credentials(profile=profile)
        for verb in self.AUTHENTICATED_LIST_EXPECTED_RESPONSES:
            self.assertEqual(getattr(self.api_client, verb)(self.RESOURCE_LIST_URI, format='json').status_code,
                             self.AUTHENTICATED_LIST_EXPECTED_RESPONSES[verb])

    def _test_details_responses_unauthenticated(self):
        detail_resource_uri = "{0}{1}/".format(self.RESOURCE_LIST_URI, self.OBJECT_ID)
        for verb in self.DETAIL_EXPECTED_RESPONSES:
            print(verb, self.LIST_EXPECTED_RESPONSES[verb])
            self.assertEqual(getattr(self.api_client, verb)(detail_resource_uri, format='json').status_code,
                             self.DETAIL_EXPECTED_RESPONSES[verb])

    def _test_details_responses_authenticated(self, profile):
        self.set_credentials(profile=profile)
        detail_resource_uri = "{0}{1}/".format(self.RESOURCE_LIST_URI, self.OBJECT_ID)
        for verb in self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES:
            resp = getattr(self.api_client, verb)(detail_resource_uri, format='json')
            self.assertEqual(resp.status_code,
                             self.AUTHENTICATED_DETAIL_EXPECTED_RESPONSES[verb])

    def run_base_tests(self, profile=None):
        """
            Run the basic tests.
            If a profile is passed, it will be used in all tests that require authentication
        :param profile: Profile
        """
        self._test_list_responses_unauthenticated()
        self._test_list_responses_authenticated(profile)
        self._test_details_responses_unauthenticated()
        self._test_details_responses_authenticated(profile)
