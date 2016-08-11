from django.db import models
from model_utils.models import TimeStampedModel
from calls import models as calls_models


# Create your models here.


class BasketItem(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    # these values are 'frozen' so no FKs
    # improves legibility
    type = models.IntegerField()
    type_name = models.CharField(max_length=40)
    # pricing
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price_vat_rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Basket(TimeStampedModel):
    CallID = models.ForeignKey(calls_models.Call)
    BasketItemID = models.ForeignKey(BasketItem, related_name='basket_basket_id_fk')


class BasketMedicine(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basketmedicine_basketitem_fk')
    # everything must be frozen at time of insert, no FKs
    active_substance = models.CharField(max_length=100, blank=True)
    package_type = models.CharField(max_length=50, unique=True)
    dispensing_unit = models.CharField(max_length=50, unique=True)
    total_dispensing_units_in_package = models.IntegerField(default=0)
    controlled_substance = models.BooleanField(default=False)
    vaccine = models.BooleanField(default=False)
    instructions = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'basket medicine'


class BasketProcedure(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basketprocedure_basket_fk')
    duration = models.IntegerField()

    def __str__(self):
        return 'basket procedure'


class BasketSupply(TimeStampedModel):
    class Meta:
        verbose_name_plural = "basket supplies"
    basket_item = models.ForeignKey(BasketItem, related_name='basketsupply_basketitem_fk')

    def __str__(self):
        return 'basket supply'


class BasketFood(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basketfood_basket_fk')
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    nutrition = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'basket food'


class BasketLaboratoryAnalysis(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basketlaboratoryanalysis_basket_fk')
    sample = models.CharField(max_length=50)

    def __str__(self):
        return 'basket laboratory'
