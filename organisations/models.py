from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    class Meta:
        verbose_name_plural = "companies"

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True)
    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Practice(TimeStampedModel):
    name = models.CharField(max_length=30)
    streetaddress = models.CharField(max_length=100, blank=True)
    streetaddress2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name


class Location(TimeStampedModel):
    name = models.CharField(max_length=50)
    practice = models.ForeignKey(Practice)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
