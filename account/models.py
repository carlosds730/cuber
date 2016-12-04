from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField


class Profile(models.Model):
    RESOURCE_NAME = 'profile'

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    photo = ImageField(upload_to='users/%Y/%m/%d',
                       blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
