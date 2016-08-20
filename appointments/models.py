from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from visitors import models as visitors_models
from smart_selects.db_fields import ChainedManyToManyField
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
    reason = models.CharField(max_length=500)
    client = models.ForeignKey(visitors_models.Client)
    # patients = models.ManyToManyField(visitors_models.Patient)

    patients = ChainedManyToManyField(
        visitors_models.Patient,
        chained_field="client",
        chained_model_field="client",
        auto_choose=True,
    )
    attending_staff = models.ForeignKey(User, blank=True, null=True)
    duration = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='appointments_created')
    modified_by = models.ForeignKey(User, related_name='appointments_modified')

    @property
    def css_status_class(self):
        if self.status == self.STATUS_UPCOMING:
            css_status = 'default'

        elif self.status == self.STATUS_ARRIVED:
            css_status = 'warning'

        elif self.status == self.STATUS_IN_CONSULT:
            css_status = 'success'

        elif self.status == self.STATUS_WAITING_TO_PAY:
            css_status = 'danger'

        elif self.status == self.STATUS_PAYMENT_COMPLETE:
            css_status = 'info'

        else:
            css_status = 'info'
        return css_status

    @property
    def css_next_step_class(self):
        if self.status == self.STATUS_UPCOMING:
            css_next_step = self.STATUS_ARRIVED

        elif self.status == self.STATUS_ARRIVED:
            css_next_step = self.STATUS_IN_CONSULT

        elif self.status == self.STATUS_IN_CONSULT:
            css_next_step = self.STATUS_WAITING_TO_PAY

        elif self.status == self.STATUS_WAITING_TO_PAY:
            css_next_step = self.STATUS_PAYMENT_COMPLETE
        else:
            css_next_step = ''
        return css_next_step

    # def get_absolute_url(self):
    #    return reverse('appointments:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.reason)
