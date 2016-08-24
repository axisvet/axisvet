from django.db import models
from django.contrib.auth.models import User
from visitors.models import Client, Patient
from django.utils.translation import ugettext as _
from smart_selects.db_fields import ChainedManyToManyField
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Status(TimeStampedModel):
    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    status = models.CharField(max_length=20)


class Consultation(TimeStampedModel):
    class Meta:
        verbose_name = _('Consultation')
        verbose_name_plural = _('Consultations')

    PAGE_ICONS = ['stethoscope']

    VERBOSE_CLIENT = Patient.VERBOSE_CLIENT
    VERBOSE_PATIENTS = Client.VERBOSE_PATIENTS
    VERBOSE_START = _('Consult Start')
    VERBOSE_FINISH = _('Consult Finish')
    VERBOSE_ATTENDING_STAFF = _('Vet/Nurse')
    VERBOSE_CREATED_BY = _('Created by')
    VERBOSE_MODIFIED_BY = _('Last updated by')
    client = models.ForeignKey(Client, verbose_name=VERBOSE_CLIENT)
    patients = ChainedManyToManyField(
        Patient,
        chained_field="client",
        chained_model_field="client",
        auto_choose=True,
        verbose_name=VERBOSE_PATIENTS
    )
    start = models.DateTimeField(verbose_name=VERBOSE_START)
    finish = models.DateTimeField(blank=True, null=True, verbose_name=VERBOSE_FINISH)
    attending_staff = models.ForeignKey(User, verbose_name=VERBOSE_ATTENDING_STAFF)
    created_by = models.ForeignKey(User, related_name='consultations_created', verbose_name=VERBOSE_CREATED_BY)
    modified_by = models.ForeignKey(User, related_name='consultations_modified', verbose_name=VERBOSE_MODIFIED_BY)

    # automatically called by CreateView and UpdateView, no need to use success_url in view
    def get_absolute_url(self):
        return reverse('consultations:detail', kwargs={'pk': self.pk})

    def __str__(self):
        patients = ', '.join([str(name) for name in self.patients.all()])
        return '%s (%s)' % (patients, self.client)

    # table headers titles on consultation listview page (rendered in templates/list.html)
    @property
    def get_listview_headers(self):
        verbose_fields = [
            self.VERBOSE_PATIENTS,
            self.VERBOSE_CLIENT,
            Observation.VERBOSE_OBSERVATION,
            self.VERBOSE_START,
            self.VERBOSE_ATTENDING_STAFF,
        ]
        return verbose_fields


class Observation(TimeStampedModel):

    class Meta:
        verbose_name = _('Observation')
        verbose_name_plural = _('Observations')

    VERBOSE_OBSERVATION = _('Observations')

    consultation = models.ForeignKey(Consultation)
    observation = models.CharField(max_length=1000, verbose_name=VERBOSE_OBSERVATION)

    def __str__(self):
        return self.observation


class ClinicalNotes(TimeStampedModel):
    class Meta:
        verbose_name = _('Clinical Notes')
        verbose_name_plural = _('Clinical Notes')

    VERBOSE_CLINICAL_NOTES = _('Clinical Notes')

    consultation = models.ForeignKey(Consultation)
    clinical_notes = models.CharField(max_length=1000, verbose_name=VERBOSE_CLINICAL_NOTES)

    def __str__(self):
        return self.clinical_notes


class Diagnosis(TimeStampedModel):
    class Meta:
        verbose_name = _('Diangosis')
        verbose_name_plural = _('Diagnoses')

    VERBOSE_DIAGNOSIS = _('Diagnosis')

    consultation = models.ForeignKey(Consultation)
    diagnosis = models.CharField(max_length=1000, verbose_name=VERBOSE_DIAGNOSIS)

    def __str__(self):
        return self.diagnosis


class TreatmentPlan(TimeStampedModel):
    class Meta:
        verbose_name = _('Treatment Plan')
        verbose_name_plural = _('Treatment Plans')

    VERBOSE_TREATMENT_PLAN = _('Treatment Plan')
    consultation = models.ForeignKey(Consultation)
    treatment_plan = models.CharField(max_length=1000, verbose_name=VERBOSE_TREATMENT_PLAN)

    def __str__(self):
        return self.treatment_plan
