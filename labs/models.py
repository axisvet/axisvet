from django.db import models
from model_utils.models import TimeStampedModel
from items.models import Item
from visitors.models import Species


# units values for results e.g. mg/L
# used in panel tests and analyses
class LabUnit(TimeStampedModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# group of related tests - tests cannot be bought, only the panel
# so panels must reference the Item model
class Panel(TimeStampedModel):
    name = models.ForeignKey(Item, limit_choices_to={'type': Item.ITEM_PANEL})

    def __str__(self):
        return str(self.name)


class Analysis(TimeStampedModel):
    name = models.ForeignKey(Item, limit_choices_to={'type': Item.ITEM_ANALYSIS})

    def __str__(self):
        return str(self.name)


# tests belonging to a Panel parent (tests are not Items, panels are)
class PanelTest(TimeStampedModel):
    panel = models.ForeignKey(Panel)
    name = models.CharField(max_length=30, unique=True)
    unit = models.ForeignKey(LabUnit)

    def __str__(self):
        return self.name


# mixin to create references tables
class Reference(TimeStampedModel):
    min = models.DecimalField(max_digits=6, decimal_places=2)
    max = models.DecimalField(max_digits=6, decimal_places=2)
    species = models.ForeignKey(Species)

    class Meta:
        abstract = True


class PanelTestRange(Reference):
    panel = models.ForeignKey(PanelTest)

    def __str__(self):
        r = 'pr child'
        return r


class AnalysisRange(Reference):
    analysis = models.ForeignKey(Analysis)

    def __str__(self):
        r = 'ar child'
        return r
