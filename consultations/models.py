from django.db import models
from django.contrib.auth.models import User
from visitors import models as visitors_models
from items import models as items_models


from model_utils.models import TimeStampedModel

# Create your models here.

class Status(TimeStampedModel):
    class Meta:
        verbose_name_plural = "status"
    status = models.CharField(max_length=20)

class Consultation(TimeStampedModel):
    client = models.ForeignKey(visitors_models.Client)
    patient = models.ManyToManyField(visitors_models.Patient)
    arrival_time = models.DateTimeField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    attending_staff = models.ForeignKey(User)
    #maybe just update appointment status -> waiting to pay when consult finishes?
    #status = models.ForeignKey(Status)
    def __str__(self):
        patients = ', '.join([str(name) for name in self.patient.all()])
        #return '%s %s (%s)' % (self.arrival_time, patients, self.client)
        #return self.arrival_time
        return patients

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


#shopping basket of items
class Item(TimeStampedModel):
    consultation = models.ForeignKey(Consultation)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_with_vat = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    #type = models.ForeignKey(items_models.ItemType, related_name='c_i_type_code')
    #maybe freeze the type code e.g. medicine, to record what vet actually selected at that moment
    def __str__(self):
        return self.name

