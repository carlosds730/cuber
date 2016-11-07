from django.db import models

from base.models import PrimaryModel, BaseImage


class Car(PrimaryModel):
    RESOURCE_NAME = 'car'

    brand = models.CharField(max_length=250)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return ' '.join([self.brand, str(self.year)])


class Driver(PrimaryModel):
    class Meta:
        ordering = ('rate',)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    id_number = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cars = models.ManyToManyField(Car, related_name='drivers', blank=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])


class Image(BaseImage):
    # Related fields
    related_car = models.ForeignKey(Car, related_name='pictures', null=True, blank=True)
    related_driver = models.ForeignKey(Driver, related_name='images', null=True, blank=True)
