from django.contrib import admin
from .models import Panel, PanelTest, PanelTestRange,\
    Analysis, AnalysisRange

#inline display to add/edit non-sellable test names (e.g. WBC) & min/max values
class PanelTestInline(admin.TabularInline):
    show_change_link = True
    model = PanelTest
    extra = 1

class PanelTestRangeInline(admin.TabularInline):
    show_change_link = True
    model = PanelTestRange
    extra = 1


class PanelAdmin(admin.ModelAdmin):
    #list_display = ['name']
    list_filter = ['name']
    inlines = [PanelTestInline]


class PanelTestAdmin(admin.ModelAdmin):
    #list_display = ['name']
    list_filter = ['name']
    inlines = [PanelTestRangeInline]


class AnalysisRangeInline(admin.TabularInline):
    show_change_link = True
    model = AnalysisRange
    extra = 1


class AnalysisAdmin(admin.ModelAdmin):
    #list_display = ['name']
    list_filter = ['name']
    inlines = [AnalysisRangeInline]




admin.site.register(Panel, PanelAdmin)
admin.site.register(PanelTest, PanelTestAdmin)
admin.site.register(Analysis, AnalysisAdmin)
