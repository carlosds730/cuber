from django.db import models
from base.models import PrimaryModel
from taxi.models import Car, Driver


class Travel(PrimaryModel):
    when = models.DateTimeField()
    car = models.ForeignKey(Car, related_name='travels')
    driver = models.ForeignKey(Driver, related_name='travels')
    duration = models.PositiveSmallIntegerField()


class TravelRequest(PrimaryModel):
    when = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    travel = models.OneToOneField(Travel, related_name='request')


class TravelConfirmation(PrimaryModel):
    travel = models.OneToOneField(TravelRequest, related_name='confirmation', null=True, blank=True)
    confirmation_text = models.CharField(max_length=250)
