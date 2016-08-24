from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from visitors.models import Client, Patient
from consultations.models import Consultation
from smart_selects.db_fields import ChainedManyToManyField
from model_utils.models import TimeStampedModel


class Appointment(TimeStampedModel):
    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    PAGE_ICONS = ['calendar']

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

    VERBOSE_STATUS = _('Status')
    VERBOSE_START = _('Date/Time')
    VERBOSE_REASON = _('Reason')
    VERBOSE_CLIENT = Patient.VERBOSE_CLIENT
    VERBOSE_PATIENTS = Client.VERBOSE_PATIENTS
    VERBOSE_DURATION = _('Duration')
    VERBOSE_ATTENDING_STAFF = Consultation.VERBOSE_ATTENDING_STAFF
    VERBOSE_CONSULTATION = _('Consultation')
    VERBOSE_CREATED_BY = Consultation.VERBOSE_CREATED_BY
    VERBOSE_MODIFIED_BY = Consultation.VERBOSE_MODIFIED_BY

    status = models.CharField(choices=STATUS_CHOICES, max_length=50, verbose_name=VERBOSE_STATUS)
    start = models.DateTimeField(verbose_name=VERBOSE_START)
    reason = models.CharField(max_length=500, verbose_name=VERBOSE_REASON)
    client = models.ForeignKey(Client, verbose_name=VERBOSE_CLIENT)
    patients = ChainedManyToManyField(
        Patient,
        chained_field="client",
        chained_model_field="client",
        auto_choose=True,
        verbose_name=VERBOSE_PATIENTS
    )
    duration = models.IntegerField(verbose_name=VERBOSE_DURATION)
    attending_staff = models.ForeignKey(User, blank=True, null=True, verbose_name=VERBOSE_ATTENDING_STAFF)
    consultation = models.OneToOneField(Consultation, blank=True, null=True,
                                        related_name='app_con', verbose_name=VERBOSE_CONSULTATION)
    created_by = models.ForeignKey(User, related_name='appointments_created', verbose_name=VERBOSE_CREATED_BY)
    modified_by = models.ForeignKey(User, related_name='appointments_modified', verbose_name=VERBOSE_MODIFIED_BY)

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

    # table headers titles on appointment listview page (rendered in templates/list.html)
    @property
    def get_listview_headers(self):
        verbose_fields = [
            self.VERBOSE_PATIENTS,
            self.VERBOSE_CLIENT,
            self.VERBOSE_START,
            self.VERBOSE_ATTENDING_STAFF,
            self.VERBOSE_REASON
        ]
        return verbose_fields

    # automatically called by CreateView and UpdateView, no need to use success_url in view
    def get_absolute_url(self):
        return reverse('appointments:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.reason)
