from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel
from visitors.models import Client

class Basket(TimeStampedModel):
    BASKET_TYPE_CONSULTATION = 'consultation'
    BASKET_TYPE_COUNTER_SALE = 'counter sale'
    BASKET_TYPE_ESTIMATE = 'estimate'
    BASKET_TYPE_REPEAT_PRESCRIPTION = 'repeat prescription'
    BASKET_TYPE_WEB_SALE = 'web sale'

    BASKET_TYPE_CHOICES = (
        (BASKET_TYPE_CONSULTATION, _('Consultation')),
        (BASKET_TYPE_COUNTER_SALE, _('Counter Sale')),
        (BASKET_TYPE_ESTIMATE, _('Estimate')),
        (BASKET_TYPE_REPEAT_PRESCRIPTION, _('Repeat Prescription')),
        (BASKET_TYPE_WEB_SALE, _('Web Sale')),
    )

    type = models.CharField(choices=BASKET_TYPE_CHOICES, max_length=50)

    @property
    def total_sale_price(self):
        return self.items.aggregate(models.Sum('sale_price'))

    # client = models.ForeignKey(Client)


class BasketItem(TimeStampedModel):
    basket = models.ForeignKey(Basket, related_name='basket_items')
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    # these values are 'frozen' so no FKs
    type = models.IntegerField()
    type_name = models.CharField(max_length=40)
    # pricing
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price_vat_rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class BasketMedicine(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basket_medicines')
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
    basket_item = models.ForeignKey(BasketItem, related_name='basket_procedures')
    duration = models.IntegerField()

    def __str__(self):
        return 'basket procedure'


class BasketSupply(TimeStampedModel):
    class Meta:
        verbose_name_plural = "basket supplies"

    basket_item = models.ForeignKey(BasketItem, related_name='basket_supplies')

    def __str__(self):
        return 'basket supply'


class BasketFood(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basket_foods')
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    nutrition = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'basket food'


class BasketAnalysis(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basket_analyses')
    sample = models.CharField(max_length=50)

    def __str__(self):
        return 'basket analysis'

class BasketPanel(TimeStampedModel):
    basket_item = models.ForeignKey(BasketItem, related_name='basket_panels')
    sample = models.CharField(max_length=50)

    def __str__(self):
        return 'basket panel'