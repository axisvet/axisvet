from django.db import models
from model_utils.models import TimeStampedModel
from items import models as items_models
from visitors import models as visitors_models


# Register your models here.


class LaboratoryPanel(TimeStampedModel):
    #only display items of type 'Laboratory Panel' from table Items, I have hardcoded ID=6 for now,
    # but want to use more robust, maybe match class name to a constant 'LaboratoryPanel' saved for
    # that Item type - suggestions welcome :)
    name = models.ForeignKey(items_models.Item, limit_choices_to={'type': 6} )
    def __str__(self):
        return str(self.name)

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


class LaboratoryAnalysisReferenceValue(TimeStampedModel):
    analysis = models.ForeignKey(LaboratoryPanel)
    species = models.ForeignKey(visitors_models.Species)
    unit = models.ForeignKey(LaboratoryAnalysisUnit)
    min = models.DecimalField(max_digits=6, decimal_places=2)
    max = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.analysis.item.name



class LaboratoryPanelReferenceValue(TimeStampedModel):
    panel = models.ForeignKey(LaboratoryPanel)
    analysis = models.CharField(max_length=50)
    species = models.ForeignKey(visitors_models.Species)
    unit = models.ForeignKey(LaboratoryAnalysisUnit)
    min = models.DecimalField(max_digits=6, decimal_places=2)
    max = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        #return '%s (%s)' % (self.analysis,self.panel)
        r = "{0} for {1} ({2}) ".format(self.analysis, self.species, self.panel)
        return r
