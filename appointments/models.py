from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from visitors import models as visitors_models
from consultations import models as consultation_models
from organisations import models as organisation_models

# Create your models here.
from model_utils.models import TimeStampedModel

class AppointmentStatus(TimeStampedModel):
    class Meta:
        verbose_name_plural = "appointment status"
    status = models.CharField(max_length=20)
    def __str__(self):
        return (self.status)

class Appointment(TimeStampedModel):
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.CharField(max_length=500)
    patient = models.ManyToManyField(visitors_models.Patient)
    attending_staff = models.ForeignKey(User)
    status = models.ForeignKey(AppointmentStatus)
    client = models.ForeignKey(visitors_models.Client)
    duration = models.IntegerField()
    consultation = models.ForeignKey(consultation_models.Consultation, blank=True, null=True)
    practice = models.ForeignKey(organisation_models.Practice)
    createdby = models.ForeignKey(User, related_name='a_u_createdby')
    modifiedby = models.ForeignKey(User, related_name='a_u_modifiedby')
    def __str__(self):
        return str(self.reason)

