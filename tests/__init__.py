from django.test import TestCase
from django.contrib.auth.models import User
from account.models import Profile
from util.utils import get_random_user_name
from random import randint


class BasicTest(TestCase):
    @staticmethod
    def create_user(user_name=get_random_user_name(), password=randint(10000000, 99999999), email=None):
        return Profile.objects.create(user=User.objects.create_user(user_name, email=email, password=password))
