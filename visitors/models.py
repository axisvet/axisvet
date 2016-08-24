from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel
from django.urls import reverse


class Species(TimeStampedModel):
    class Meta:
        verbose_name = "Species"
        verbose_name_plural = "Species"

    name = models.CharField(max_length=30, verbose_name=_('Species name'))
    species_code = models.CharField(max_length=30, verbose_name=_('Unique ID code'))

    def __str__(self):
        return self.name


class Client(TimeStampedModel):
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    PAGE_ICONS = ['group']

    VERBOSE_FIRST_NAME = _('First Name')
    VERBOSE_LAST_NAME = _('Last Name')
    VERBOSE_EMAIL = _('Email')
    VERBOSE_STREET_ADDRESS = _('Address Line 1')
    VERBOSE_STREET_ADDRESS_2 = _('Address Line 2')
    VERBOSE_CITY = _('Town / City')
    VERBOSE_ZIP = _('Postcode')
    VERBOSE_COUNTY = _('County / State')
    VERBOSE_MOBILE = _('Mobile Phone')
    VERBOSE_ORGANISATION_NAME = _('Company')
    VERBOSE_REMARKS = _('Remarks')

    # custom verbose names for use in template displays #
    VERBOSE_FULL_NAME = _('Client')
    VERBOSE_PATIENTS = _('Animals')

    first_name = models.CharField(max_length=30, verbose_name=VERBOSE_FIRST_NAME)
    last_name = models.CharField(max_length=30, verbose_name=VERBOSE_LAST_NAME)
    email = models.EmailField(max_length=50, blank=True, verbose_name=VERBOSE_EMAIL)
    street_address = models.CharField(max_length=100, blank=True, verbose_name=VERBOSE_STREET_ADDRESS)
    street_address_2 = models.CharField(max_length=100, blank=True, verbose_name=VERBOSE_STREET_ADDRESS_2)
    city = models.CharField(max_length=30, blank=True, verbose_name=VERBOSE_CITY)
    zip = models.CharField(max_length=10, blank=True, verbose_name=VERBOSE_ZIP)
    county = models.CharField(max_length=30, blank=True, verbose_name=VERBOSE_COUNTY)
    mobile = models.CharField(max_length=20, verbose_name=VERBOSE_MOBILE)
    organisation_name = models.CharField(max_length=50, blank=True, verbose_name=VERBOSE_ORGANISATION_NAME)
    remarks = models.CharField(max_length=200, blank=True, verbose_name=VERBOSE_REMARKS)

    # automatically called by CreateView and UpdateView, no need to use success_url in view
    def get_absolute_url(self):
        return reverse('visitors:client_detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return ''.join(
            [self.first_name, ' ', self.last_name])

    # table headers titles on patient listview page (rendered in templates/list.html)
    @property
    def get_listview_headers(self):
        verbose_fields = [
            self.VERBOSE_FULL_NAME,
            self.VERBOSE_PATIENTS,
            self.VERBOSE_STREET_ADDRESS,
            self.VERBOSE_MOBILE,
        ]
        return verbose_fields

    def __str__(self):
        return self.full_name


class Patient(TimeStampedModel):
    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    PAGE_ICONS = ['dog', 'cat', 'rabbit']
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

    VERBOSE_GENDER = _('Male / Female')
    VERBOSE_CLIENT = _('Owner')
    VERBOSE_NAME = _('Name')
    VERBOSE_SPECIES = _('Species')
    VERBOSE_BREED = _('Breed')
    VERBOSE_WEIGHT = _('Weight (kg)')
    VERBOSE_DATE_OF_BIRTH = _('Date of Birth')
    VERBOSE_COLOUR = _('Colour / Markings')
    VERBOSE_REMARKS = _('Remarks')
    VERBOSE_MICROCHIP = _('Microchip ID')
    VERBOSE_ARCHIVED = _('Archived')
    VERBOSE_DECEASED = _('Deceased')

    # custom verbose names for use in template displays #
    #

    gender = models.CharField(choices=PATIENT_GENDER_CHOICES, max_length=50, verbose_name=VERBOSE_GENDER)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='patients', verbose_name=VERBOSE_CLIENT)
    name = models.CharField(max_length=30, verbose_name=VERBOSE_NAME)
    species = models.ForeignKey(Species, verbose_name=VERBOSE_SPECIES)
    breed = models.CharField(max_length=30, blank=True, verbose_name=VERBOSE_BREED)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name=VERBOSE_WEIGHT)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=VERBOSE_DATE_OF_BIRTH)
    colour = models.CharField(max_length=30, blank=True, verbose_name=VERBOSE_COLOUR)
    remarks = models.CharField(max_length=200, blank=True, verbose_name=VERBOSE_REMARKS)
    microchip = models.CharField(max_length=30, blank=True, verbose_name=VERBOSE_MICROCHIP)
    archived = models.BooleanField(default=False, verbose_name=VERBOSE_ARCHIVED)
    deceased = models.BooleanField(default=False, verbose_name=VERBOSE_DECEASED)

    # automatically called by CreateView and UpdateView, no need to use success_url in view
    def get_absolute_url(self):
        return reverse('visitors:patient_detail', kwargs={'pk': self.pk})

    # table headers titles on patient listview page (rendered in templates/list.html)
    @property
    def get_listview_headers(self):
        verbose_fields = [
            self.VERBOSE_SPECIES,
            self.VERBOSE_NAME,
            self.VERBOSE_WEIGHT,
            self.VERBOSE_BREED,
            self.VERBOSE_CLIENT
        ]
        return verbose_fields

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
