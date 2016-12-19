from django.db import models
from sorl.thumbnail import ImageField
from cuber.settings import API_ENTRY_POINT, API_NAME


class PrimaryModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    RESOURCE_NAME = None

    # Tastypie related methods and functions.
    # The functionality of this methods is the same as ModelResource,get_resource_uri
    # they are replicated here for simplification.
    @classmethod
    def resource_list_uri(cls):
        if not cls.RESOURCE_NAME:
            return None
        return "{0}{1}/".format(API_ENTRY_POINT, cls.RESOURCE_NAME)

    @classmethod
    def _resource_detail_uri(cls, object_id):
        if not cls.RESOURCE_NAME or not object_id:
            return None
        return "{0}{1}/".format(cls.resource_list_uri(), object_id)

    @property
    def resource_detail_uri(self):
        return self._resource_detail_uri(self.id)

    class Meta:
        abstract = True


class BaseModelWithStatus(PrimaryModel):
    STATUS_CREATED = 0
    STATUS_CHOICES = [(STATUS_CREATED, 'Created')]
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_CREATED)

    class Meta:
        abstract = True


class BaseImage(PrimaryModel):
    picture = ImageField(upload_to='pictures')
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.description
