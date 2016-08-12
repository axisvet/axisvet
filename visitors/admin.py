from django.contrib import admin
from django.db.models import Prefetch
# Register your models here.
from .models import Client, Patient, PatientGender, Species


class PatientInline(admin.StackedInline):
    model = Patient
    extra = 1
    exclude = ['deceased', 'archived']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'get_patients')
    #now only makes one query, not 100 per page :)
    def get_queryset(self, obj):
        qs = super(ClientAdmin, self).get_queryset(obj)
        return qs.prefetch_related('patient_fk')

    def get_patients(self, obj):
        return list(obj.patient_fk.all())

    search_fields = ['first_name', 'last_name', 'street_address', 'zip', 'mobile', 'patient_fk__name']
    inlines = [PatientInline]


admin.site.register(Client, ClientAdmin)


class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ['client']
    # raw_id_fields = ("client",)
    list_display = ('name', 'species', 'breed', 'gender')
    list_filter = ['species', 'breed', 'gender']
    search_fields = ['name', 'breed']


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientGender)
admin.site.register(Species)
