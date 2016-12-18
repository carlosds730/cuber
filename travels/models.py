from django.db import models
from base.models import PrimaryModel, BaseModelWithStatus
from taxi.models import Car, Driver
from account.models import Profile


class Travel(BaseModelWithStatus):
    STATUS_DRIVERS_FAULT = -3  # The Driver didn't show
    STATUS_NO_SHOW = -2  # The Client didn't show
    STATUS_CANCELED = -1  # The Client cancelled the travel after the TravelRequest was confirmed

    STATUS_COMPLETED = 1

    STATUS_CHOICES = BaseModelWithStatus.STATUS_CHOICES + [
        (STATUS_DRIVERS_FAULT, 'Driver\'s fault'),
        (STATUS_NO_SHOW, 'No show'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    when = models.DateTimeField()
    assigned_car = models.ForeignKey(Car, related_name='travels')
    assigned_driver = models.ForeignKey(Driver, related_name='travels')
    duration = models.PositiveSmallIntegerField(verbose_name='Duration', help_text='Travel duration (in hours)')
    client = models.ForeignKey(Profile, related_name='travels')
    rating = models.PositiveSmallIntegerField(verbose_name='Rating', null=True, blank=True)


class TravelRequest(BaseModelWithStatus):
    RESOURCE_NAME = 'travelrequest'
    STATUS_DISMISSED = -3  # When the taxi's owner said Yes, but the client didn't confirm
    STATUS_CANCELED = -2  # When the client cancels
    STATUS_FAILED = -1  # When the taxi owner says No
    STATUS_PENDING_CONFIRMATION_FROM_TAXI_OWNER = 1  # Waiting for the taxi's owner to respond
    STATUS_CONFIRMED_FROM_TAXI_OWNER = 2  # Confirmed by the taxi's owner
    STATUS_PENDING_CONFIRMATION_FROM_CLIENT = 3  # Waiting for the client to confirm
    STATUS_CONFIRMED = 4  # Both taxi's owner and client have confirmed

    STATUS_CHOICES = BaseModelWithStatus.STATUS_CHOICES + [(STATUS_DISMISSED, 'Dismissed'),
                                                           (STATUS_CANCELED, 'Canceled'),
                                                           (STATUS_FAILED, 'Failed'),
                                                           (STATUS_PENDING_CONFIRMATION_FROM_TAXI_OWNER,
                                                            'Pending confirmation from taxi\'s owner'),
                                                           (STATUS_CONFIRMED_FROM_TAXI_OWNER,
                                                            'Confirmed from taxi\'s owner'),
                                                           (STATUS_PENDING_CONFIRMATION_FROM_CLIENT,
                                                            'Pending confirmation from the client'),
                                                           (STATUS_CONFIRMED, 'Confirmed')
                                                           ]

    when = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(verbose_name='Duration', help_text='Travel duration (in hours)')
    travel = models.OneToOneField(Travel, related_name='request', null=True, blank=True)
    assigned_car = models.ForeignKey(Car, related_name='travels_requests', null=True, blank=True)
    assigned_driver = models.ForeignKey(Driver, related_name='requested_travels', null=True, blank=True)
    client = models.ForeignKey(Profile, related_name='requested_travels')


class TravelConfirmation(PrimaryModel):
    # Confirmation message from the taxi's owner.
    # It must contain the assigned car and the driver.
    travel_request = models.OneToOneField(TravelRequest, related_name='confirmation', null=True, blank=True)
    confirmation_text = models.CharField(max_length=250)
    assigned_car = models.ForeignKey(Car, related_name='confirmed_travels', null=True, blank=True)
    assigned_driver = models.ForeignKey(Driver, related_name='travels_confirmed', null=True, blank=True)
