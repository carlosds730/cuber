from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from django.contrib.auth.models import User
from account.models import Profile
from util.utils import get_random_name
from random import randint


class BasicAPITest(ResourceTestCaseMixin, TestCase):
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

    @staticmethod
    def create_user(user_name=get_random_name(), password=randint(10000000, 99999999), email=None):
        return Profile.objects.create(user=User.objects.create_user(user_name, email=email, password=password))
