from django.contrib import admin

# Register your models here.
from .models import Appointment, AppointmentStatus


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('reason', 'client', 'status', 'start')
    list_filter = ['status']
    date_hierarchy = 'start'
    search_fields = ['reason', 'patient__name']
    # get list of all patients for this consultation

    filter_horizontal = ['patient']

    def get_patient(self, obj):
        # return 'ok'
        #return ', '.join([str(name) for name in obj.patient.all()])
       return obj.filter(pk=1)




class AppointmentStatusAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'type_code')
    # list_filter = ['type_code']
    search_fields = ['status']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AppointmentStatus, AppointmentStatusAdmin)
