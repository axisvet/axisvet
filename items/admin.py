from django.contrib import admin

# Register your models here.
from .models import Item, ItemType, Medicine, ItemCategory, \
    VatRate, Package, Unit, SpecialProcedure, SampleType, Procedure, \
    Supply, Food, LaboratoryAnalysis


class MedicineInline(admin.StackedInline):
    model = Medicine
    max_num = 1

class ProcedureInline(admin.StackedInline):
    model = Procedure
    max_num = 1

class SupplyInline(admin.StackedInline):
    model = Supply
    max_num = 1

class FoodInline(admin.StackedInline):
    model = Food
    max_num = 1

class LaboratoryAnalysisInline(admin.StackedInline):
    model = LaboratoryAnalysis
    max_num = 1

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'sale_price')
    list_filter = ['type']
    search_fields = ['name']
    inlines = [MedicineInline, ProcedureInline, SupplyInline, FoodInline, LaboratoryAnalysisInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType)
admin.site.register(ItemCategory)
admin.site.register(VatRate)
admin.site.register(Package)
admin.site.register(Unit)
admin.site.register(SpecialProcedure)
admin.site.register(SampleType)