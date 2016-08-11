from django.contrib import admin

# Register your models here.
from .models import LaboratoryDevice, LaboratoryDeviceType, \
    LaboratoryAnalysisUnit, LaboratoryAnalysisReferenceValue, \
    LaboratoryPanelReferenceValue, LaboratoryPanel

class LaboratoryPanelReferenceValueAdmin(admin.ModelAdmin):
    list_filter = ['species', 'panel']


class LaboratoryPanelReferenceValueInline(admin.TabularInline):
    model = LaboratoryPanelReferenceValue
    extra = 1

class LaboratoryPanelAdmin(admin.ModelAdmin):
    inlines = [LaboratoryPanelReferenceValueInline]


admin.site.register(LaboratoryPanel,LaboratoryPanelAdmin)
admin.site.register(LaboratoryDevice)
admin.site.register(LaboratoryDeviceType)
admin.site.register(LaboratoryAnalysisUnit)
admin.site.register(LaboratoryAnalysisReferenceValue)
admin.site.register(LaboratoryPanelReferenceValue, LaboratoryPanelReferenceValueAdmin)
