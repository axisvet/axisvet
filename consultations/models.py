from django.db import models
from django.contrib.auth.models import User
from visitors import models as visitors_models
from smart_selects.db_fields import ChainedManyToManyField
from django.utils.timezone import now
from model_utils.models import TimeStampedModel


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
    start = models.DateTimeField()
    finish = models.DateTimeField(blank=True, null=True)
    attending_staff = models.ForeignKey(User)
    created_by = models.ForeignKey(User, related_name='consultations_created')
    modified_by = models.ForeignKey(User, related_name='consultations_modified')

    def __str__(self):
        patients = ', '.join([str(name) for name in self.patients.all()])
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
