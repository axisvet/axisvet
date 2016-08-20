from django.db import models
from django.contrib.auth.models import User
from visitors import models as visitors_models
from smart_selects.db_fields import ChainedManyToManyField

from model_utils.models import TimeStampedModel


# Create your models here.

class Status(TimeStampedModel):
    class Meta:
        verbose_name_plural = "status"

    status = models.CharField(max_length=20)


class Consultation(TimeStampedModel):
    client = models.ForeignKey(visitors_models.Client)
    # patient = models.ManyToManyField(visitors_models.Patient)

    patients = ChainedManyToManyField(
        visitors_models.Patient,
        chained_field="client",
        chained_model_field="client",
        auto_choose=True,
    )
    arrival_time = models.DateTimeField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    attending_staff = models.ForeignKey(User)

    # maybe just update appointment status -> waiting to pay when consult finishes?
    # status = models.ForeignKey(Status)
    def __str__(self):
        patients = ', '.join([str(name) for name in self.patient.all()])
        # return '%s %s (%s)' % (self.arrival_time, patients, self.client)
        # return self.arrival_time
        return 'patients in consult: %s with %s' % (patients, self.client)


class Observation(TimeStampedModel):
    consultation = models.ForeignKey(Consultation)
    observation = models.CharField(max_length=1000)

    def __str__(self):
        return self.observation


class ClinicalNotes(TimeStampedModel):
    class Meta:
        verbose_name_plural = "clinical notes"

    consultation = models.ForeignKey(Consultation)
    clinical_notes = models.CharField(max_length=1000)

    def __str__(self):
        return self.clinical_notes


class Diagnosis(TimeStampedModel):
    class Meta:
        verbose_name_plural = "diagnoses"

    consultation = models.ForeignKey(Consultation)
    diagnosis = models.CharField(max_length=1000)

    def __str__(self):
        return self.diagnosis


class TreatmentPlan(TimeStampedModel):
    consultation = models.ForeignKey(Consultation)
    treatment_plan = models.CharField(max_length=1000)

    def __str__(self):
        return self.treatment_plan
