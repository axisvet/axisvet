from django.db import models
from model_utils.models import TimeStampedModel
from items.models import Item
from visitors import models as visitors_models


# Register your models here.


#equipment tracking
class LaboratoryDeviceType(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class LaboratoryDevice(TimeStampedModel):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(LaboratoryDeviceType)

    def __str__(self):
        return self.name


class LaboratoryAnalysisUnit(TimeStampedModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


#lab tests and results

class Analysis(TimeStampedModel):
    name = models.ForeignKey(Item, limit_choices_to={'type':Item.ITEM_ANALYSIS})
    def __str__(self):
        return str(self.name)


class Panel(TimeStampedModel):
    name = models.ForeignKey(Item, limit_choices_to={'type':Item.ITEM_PANEL})
    def __str__(self):
        return str(self.name)


class PanelTest(TimeStampedModel):
    panel = models.ForeignKey(Panel)
    name = models.CharField(max_length=30)
    unit = models.ForeignKey(LaboratoryAnalysisUnit)
    def __str__(self):
        return "{0} ok".format(self.name)


class Reference():
    species = models.ForeignKey(visitors_models.Species)
    min = models.DecimalField(max_digits=6, decimal_places=2)
    max = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        abstract = True

    def __str__(self):
        r = "{0} for ({1}) ".format(self.panel, self.species)
        return r


class PanelReference(Reference):
    panel = models.ForeignKey(PanelTest)
    def __str__(self):
        r = 'pr child'
        return r

class AnalysisReference(Reference):
    analysis = models.ForeignKey(Analysis)
    def __str__(self):
        r = 'pr child'
        return r
