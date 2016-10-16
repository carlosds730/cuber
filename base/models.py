from django.db import models
from sorl.thumbnail import ImageField


class PrimaryModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelWithStatus(PrimaryModel):
    STATUS_CREATED = (0, 'Created')
    STATUS_CHOICES = [STATUS_CREATED]
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
