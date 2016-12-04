from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from django.contrib.auth.models import User


class BasicAPITest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super(BasicAPITest, self).setUp()

        # Create a user.
        self.username = 'daniel'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'daniel@example.com', self.password)

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)
