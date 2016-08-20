from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel


class Species(TimeStampedModel):
    class Meta:
        verbose_name_plural = "species"

    name = models.CharField(max_length=30)
    species_code = models.CharField(max_length=30)

    def __str__(self):
        return self.name


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
    PATIENT_GENDER_FEMALE = 'female'
    PATIENT_GENDER_FEMALE_STERILISED = 'female sterilised'
    PATIENT_GENDER_MALE = 'male'
    PATIENT_GENDER_MALE_STERILISED = 'male sterilised'
    PATIENT_GENDER_UNKNOWN = 'unknown'

    PATIENT_GENDER_CHOICES = (
        (PATIENT_GENDER_FEMALE, _('Female')),
        (PATIENT_GENDER_FEMALE_STERILISED, _('Female Sterilised')),
        (PATIENT_GENDER_MALE, _('Male')),
        (PATIENT_GENDER_MALE_STERILISED, _('Male Sterilised')),
        (PATIENT_GENDER_UNKNOWN, _('Unknown')),
    )

    gender = models.CharField(choices=PATIENT_GENDER_CHOICES, max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=30)
    species = models.ForeignKey(Species)
    breed = models.CharField(max_length=30, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    colour = models.CharField(max_length=30, blank=True)
    remark = models.CharField(max_length=200, blank=True)
    # insurance FK later
    microchip = models.CharField(max_length=30, blank=True)
    archived = models.BooleanField(default=False)
    deceased = models.BooleanField(default=False)

    @property
    def css_species_class(self):
        if self.species.species_code == 'DOG':
            css_species = 'dog'
        elif self.species.species_code == 'CAT':
            css_species = 'cat'
        else:
            css_species = 'question-sign'
        return css_species

    @property
    def css_gender_class(self):
        if self.gender == self.PATIENT_GENDER_FEMALE or self.gender == self.PATIENT_GENDER_FEMALE_STERILISED:
            css_gender = 'gender-female'
        elif self.gender == self.PATIENT_GENDER_MALE or self.gender == self.PATIENT_GENDER_MALE_STERILISED:
            css_gender = 'gender-male'
        else:
            css_gender = 'gender-unknown'
        return css_gender

    def __str__(self):
        return self.name
