from django.db import models
from base.models import PrimaryModel, BaseModelWithStatus
from taxi.models import Car, Driver


class Travel(BaseModelWithStatus):
    STATUS_FAILED = -1

    STATUS_COMPLETED = 1

    STATUS_CHOICES = [BaseModelWithStatus.STATUS_CREATED, STATUS_FAILED, STATUS_COMPLETED]

    when = models.DateTimeField()
    assigned_car = models.ForeignKey(Car, related_name='travels')
    assigned_driver = models.ForeignKey(Driver, related_name='travels')
    duration = models.PositiveSmallIntegerField()


class TravelRequest(BaseModelWithStatus):
    STATUS_CANCELED = -2  # When the client cancels
    STATUS_FAILED = -1  # When the taxi owner says No
    STATUS_PENDING_CONFIRMATION_FROM_TAXI_OWNER = 1  # Waiting for the taxi owner to respond
    STATUS_CONFIRMED_FROM_TAXI_OWNER = 2  # Confirmed by the taxi's owner
    STATUS_PENDING_CONFIRMATION_FROM_CLIENT = 3  # Waiting for the client to confirm
    STATUS_CONFIRMED = 4  # Both taxi's owner and client has confirmed

    STATUS_CHOICES = [BaseModelWithStatus.STATUS_CREATED, STATUS_FAILED, STATUS_PENDING_CONFIRMATION_FROM_TAXI_OWNER,
                      STATUS_CONFIRMED_FROM_TAXI_OWNER,
                      STATUS_PENDING_CONFIRMATION_FROM_CLIENT, STATUS_CONFIRMED]

    when = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    travel = models.OneToOneField(Travel, related_name='request', null=True, blank=True)


class TravelConfirmation(PrimaryModel):
    travel_request = models.OneToOneField(TravelRequest, related_name='confirmation', null=True, blank=True)
    confirmation_text = models.CharField(max_length=250)
