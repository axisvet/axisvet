from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from visitors import models as visitors_models
from organisations import models as organisation_models
from model_utils.models import TimeStampedModel


class Appointment(TimeStampedModel):
    STATUS_UPCOMING = 'upcoming'
    STATUS_ARRIVED = 'arrived'
    STATUS_IN_CONSULT = 'in consult'
    STATUS_WAITING_TO_PAY = 'waiting to pay'
    STATUS_PAYMENT_COMPLETE = 'payment complete'

    STATUS_CHOICES = (
        (STATUS_UPCOMING, _('Upcoming')),
        (STATUS_ARRIVED, _('Arrived')),
        (STATUS_IN_CONSULT, _('In Consult')),
        (STATUS_WAITING_TO_PAY, _('Waiting to Pay')),
        (STATUS_PAYMENT_COMPLETE, _('Payment Complete')),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.CharField(max_length=500)
    patients = models.ManyToManyField(visitors_models.Patient)
    attending_staff = models.ForeignKey(User)
    client = models.ForeignKey(visitors_models.Client)
    duration = models.IntegerField()
    practice = models.ForeignKey(organisation_models.Practice)
    created_by = models.ForeignKey(User, related_name='appointments_created')
    modified_by = models.ForeignKey(User, related_name='appointments_modified')

    def __str__(self):
        return str(self.reason)
