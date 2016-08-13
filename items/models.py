from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel
from organisations import models as organisations_models
from visitors import models as visitors_models


# Create your models here.

class SpecialProcedure(TimeStampedModel):
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

    ITEM_PROCEDURE = 'procedure'
    ITEM_MEDICINE = 'medicine'
    ITEM_SUPPLY = 'supply'
    ITEM_FOOD = 'food'
    ITEM_ANALYSIS = 'analysis'
    ITEM_PANEL = 'panel'

    ITEM_TYPE_CHOICES = (
        (ITEM_PROCEDURE, _('Procedure')),
        (ITEM_MEDICINE, _('Medicine')),
        (ITEM_SUPPLY, _('Supply')),
        (ITEM_FOOD, _('Food')),
        (ITEM_ANALYSIS, _('Analysis')),
        (ITEM_PANEL, _('Panel')),
    )

    type = models.CharField(choices=ITEM_TYPE_CHOICES, max_length=50)
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, blank=True)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_price_vat_rate = models.ForeignKey(VatRate, related_name='costpricevatrate', null=True, blank=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sale_price_vat_rate = models.ForeignKey(VatRate, related_name='salepricevatrate', null=True, blank=True)
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
        return self.item.name


class Procedure(TimeStampedModel):
    item = models.ForeignKey(Item)
    duration = models.IntegerField()

    SPECIAL_PROCEDURE_STERILISATION = 'sterilisation'
    SPECIAL_PROCEDURE_EUTHANASIA = 'euthanasia'

    SPECIAL_PROCEDURE_CHOICES = (
        (SPECIAL_PROCEDURE_STERILISATION, _('Sterilisation')),
        (SPECIAL_PROCEDURE_EUTHANASIA, _('Euthanasia')),
    )

    special_procedure = models.CharField(choices=SPECIAL_PROCEDURE_CHOICES, max_length=50)


    def __str__(self):
        return self.item.name


class Supply(TimeStampedModel):
    class Meta:
        verbose_name_plural = "supplies"

    item = models.ForeignKey(Item)

    def __str__(self):
        return self.item.name


class Food(TimeStampedModel):
    item = models.ForeignKey(Item)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    nutrition = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.item.name


class LaboratoryAnalysis(TimeStampedModel):
    class Meta:
        verbose_name_plural = "laboratory analyses"

    item = models.ForeignKey(Item)
    sample = models.ForeignKey(SampleType)

    def __str__(self):
        return self.item.name



class LaboratoryAnalysisPanel(TimeStampedModel):
    class Meta:
        verbose_name_plural = "laboratory panels"

    item = models.ForeignKey(Item)
    sample = models.ForeignKey(SampleType)

    def __str__(self):
        return self.item.name

