from django.contrib import admin

# Register your models here.
from .models import Consultation, Status, Observation, ClinicalNotes, Diagnosis, TreatmentPlan


class ObservationInline(admin.StackedInline):
    model = Observation
    max_num = 1


class ClinicalNotesInline(admin.StackedInline):
    model = ClinicalNotes
    max_num = 1


class DiagnosisInline(admin.StackedInline):
    model = Diagnosis
    extra = 1


class TreatmentPlanInline(admin.StackedInline):
    model = TreatmentPlan
    max_num = 1


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('arrival_time', 'client', 'get_patients')

    def get_patients(self, obj):
        # return obj.patients.name
        # return ', '.join([str(name) for name in self.patients.all()])
        return 'ok'

    # readonly_fields = ['client']
    # list_filter = ['type_code']
    # search_fields = ['firstname', 'lastname', 'streetaddress', 'zip', 'mobile', 'patient__name']
    inlines = [ObservationInline, ClinicalNotesInline, DiagnosisInline, TreatmentPlanInline]
    filter_horizontal = ['patients']


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Status)
admin.site.register(Observation)
admin.site.register(Diagnosis)
admin.site.register(ClinicalNotes)
admin.site.register(TreatmentPlan)
