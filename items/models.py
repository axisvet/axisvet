from django.db import models
from model_utils.models import TimeStampedModel
from organisations import models as organisations_models
from visitors import models as visitors_models


# Create your models here.

class SpecialProcedure(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ItemType(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SampleType(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ItemCategory(TimeStampedModel):
    class Meta:
        verbose_name_plural = "item categories"

    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VatRate(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Package(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Unit(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Item(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, blank=True)
    type = models.ForeignKey(ItemType)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_price_vat_rate = models.ForeignKey(VatRate, related_name='costpricevatrate')
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sale_price_vat_rate = models.ForeignKey(VatRate, related_name='salepricevatrate')
    markup = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    notes = models.CharField(max_length=500, blank=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Medicine(TimeStampedModel):
    item = models.ForeignKey(Item)
    active_substance = models.CharField(max_length=100, blank=True)
    package_type = models.ForeignKey(Package, default=0)
    dispensing_unit = models.ForeignKey(Unit, default=0)
    total_dispensing_units_in_package = models.IntegerField(default=0)
    location = models.ForeignKey(organisations_models.Location, blank=True, null=True)
    controlled_substance = models.BooleanField(default=False)
    vaccine = models.BooleanField(default=False)

    def __str__(self):
        return 'medicine'


class Procedure(TimeStampedModel):
    item = models.ForeignKey(Item)
    duration = models.IntegerField()
    special_procedure = models.ForeignKey(SpecialProcedure)

    def __str__(self):
        return 'procedure'


class Supply(TimeStampedModel):
    item = models.ForeignKey(Item)

    def __str__(self):
        return 'supply'


class Food(TimeStampedModel):
    item = models.ForeignKey(Item)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    nutrition = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'food'


class LaboratoryAnalysis(TimeStampedModel):
    item = models.ForeignKey(Item)
    sample = models.ForeignKey(SampleType)

    def __str__(self):
        return 'laboratory'


class LaboratoryAnalysisReferenceValues(TimeStampedModel):
    analysis = models.ForeignKey(LaboratoryAnalysis)
    species = models.ForeignKey(visitors_models.Species)
    min = models.DecimalField(max_digits=4, decimal_places=2)
    max = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return 'laboratory reference values'
