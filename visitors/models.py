from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class PatientGender(TimeStampedModel):
    gender = models.CharField(max_length=30)
    def __str__(self):
        return self.gender

class Client(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=100, blank=True)
    street_address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    mobile = models.CharField(max_length=20)
    organisation_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Patient(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='patient_fk')
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=20, blank=True)
    breed = models.CharField(max_length=30, blank=True)
    gender = models.ForeignKey(PatientGender)
    date_of_birth = models.DateField(blank=True, null=True)
    colour = models.CharField(max_length=30, blank=True)
    remark = models.CharField(max_length=200, blank=True)
    #insurance FK later
    microchip = models.CharField(max_length=30, blank=True)
    archived = models.BooleanField(default=False)
    deceased = models.BooleanField(default=False)
    def __str__(self):
        return self.name
