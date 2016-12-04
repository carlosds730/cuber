from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from django.contrib.auth.models import User
from account.models import Profile


class BasicAPITest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super(BasicAPITest, self).setUp()

        # Create a user.
        self.username = 'test_user'
        self.password = 'pass'
        self.email = 'test_user@cuber.com'
        self.user = Profile.objects.create(
            user=User.objects.create_user(self.username, self.email, self.password))
        self.user.save()

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)
