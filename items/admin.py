from django.contrib import admin

# Register your models here.
from .models import Item, ItemType, Medicine, ItemCategory, VatRate, Package, Unit


class MedicineInline(admin.StackedInline):
    model = Medicine
    max_num = 1


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'sale_price')
    list_filter = ['type']
    search_fields = ['name']
    inlines = [MedicineInline]


admin.site.register(Item, ItemAdmin)
# admin.site.register(ItemType)
admin.site.register(ItemCategory)
admin.site.register(VatRate)
admin.site.register(Package)
admin.site.register(Unit)
