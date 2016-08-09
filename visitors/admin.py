from django.contrib import admin
from django.db.models import Prefetch
# Register your models here.
from .models import Client, Patient, PatientGender


class PatientInline(admin.StackedInline):
    model = Patient
    extra = 1
    exclude = ['deceased', 'archived']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile')

    def get_patients(self, obj):
        p = Patient.objects.filter(client_id=obj.pk)
        return list(p)

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
