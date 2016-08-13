from django.contrib import admin

# Register your models here.
from .models import LaboratoryDevice, LaboratoryDeviceType, \
    LaboratoryAnalysisUnit, PanelTest, \
     Analysis,  Panel
'''
class PanelReferenceAdmin(admin.ModelAdmin):
    list_filter = ['species', 'panel']

class AnalysisReferenceAdmin(admin.ModelAdmin):
    list_filter = ['species', 'analysis']



class PanelTestInline(admin.TabularInline):
    show_change_link = True
    model = PanelTest
    extra = 1
    #raw_id_fields=('panel', 'name', 'unit')


class PanelReferenceline(admin.TabularInline):
    show_change_link = True
    model = PanelReference
    extra = 1

class AnalysisReferenceline(admin.TabularInline):
    show_change_link = True
    model = AnalysisReference
    extra = 1

class PanelAdmin(admin.ModelAdmin):
    #list_display = ['name']
    list_filter = ['name']
    inlines = [PanelTestInline]

class PanelTestAdmin(admin.ModelAdmin):
    list_display = ['name','unit']
    list_filter = ['panel']
    #inlines = [PanelReferenceline]




admin.site.register(Panel,PanelAdmin)
admin.site.register(LaboratoryDevice)
admin.site.register(LaboratoryDeviceType)
admin.site.register(LaboratoryAnalysisUnit)
admin.site.register(PanelTest, PanelTestAdmin)
#admin.site.register(PanelReference)
admin.site.register(Analysis)
#admin.site.register(AnalysisReferenceAdmin)
'''