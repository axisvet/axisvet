from django.contrib import admin

# Register your models here.
from .models import Basket, BasketItem, BasketMedicine, BasketProcedure, \
    BasketSupply, BasketFood, BasketAnalysis, BasketPanel

admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(BasketMedicine)
admin.site.register(BasketProcedure)
admin.site.register(BasketSupply)
admin.site.register(BasketFood)
admin.site.register(BasketAnalysis)
admin.site.register(BasketPanel)

