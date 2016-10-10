from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField


class Car(models.Model):
    brand = models.CharField(max_length=250)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return ' '.join([self.brand, str(self.year)])


class Driver(models.Model):
    class Meta:
        ordering = ('rate',)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    id_number = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cars = models.ManyToManyField(Car, related_name='drivers', blank=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])


class Image(models.Model):
    image = ImageField(upload_to='pictures')
    description = models.TextField()

    # Relationship fields
    driver = models.ForeignKey(Driver, related_name='pictures', null=True, blank=True)
    car = models.ForeignKey(Car, related_name='pictures', null=True, blank=True)

    def __str__(self):
        return self.description
