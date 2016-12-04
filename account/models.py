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

    def save(self, *args, **kwargs):
        # Check if we are updating or creating an object
        update = True if self.pk else False
        # Save the object
        super(Profile, self).save(*args, **kwargs)
        # If we are not updating, create the Api Key
        if not update:
            from tastypie.models import ApiKey
            ApiKey.objects.create(user=self.user)
