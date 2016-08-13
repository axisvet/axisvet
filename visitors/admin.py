from django.contrib import admin
from django.db.models import Prefetch
# Register your models here.
from .models import Client, Patient, Species


class PatientInline(admin.StackedInline):
    model = Patient
    extra = 1
    exclude = ['deceased', 'archived']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'street_address', 'mobile', 'get_patients')

    def get_queryset(self, obj):
        qs = super(ClientAdmin, self).get_queryset(obj)
        return qs.prefetch_related('patient_fk')

    def get_patients(self, obj):
        return list(obj.patient_fk.all())
    get_patients.short_description = 'Patient'  #Renames column head

    search_fields = ['first_name', 'last_name', 'street_address', 'zip', 'mobile', 'patient_fk__name']
    inlines = [PatientInline]

class PatientAdmin(admin.ModelAdmin):
    #readonly_fields = ['client']
    # raw_id_fields = ("client",)
    list_display = ['name','species','client']
    search_fields = ['name', 'client__first_name', 'client__last_name']
    list_filter = ['species']

admin.site.register(Client, ClientAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Species)
