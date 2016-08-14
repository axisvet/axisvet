from django.contrib import admin

# Register your models here.
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('reason', 'client', 'get_patients', 'status', 'start')
    list_filter = ['status']
    date_hierarchy = 'start'
    search_fields = ['reason', 'patients__name']
    # get list of all patients for this consultation

    filter_horizontal = ['patients']



    def get_queryset(self, request):
        qs = super(AppointmentAdmin, self).get_queryset(request)
        return qs.select_related('client')


    def get_patients(self, obj):
        # return 'ok'
        return list(obj.patients.all())

class AppointmentStatusAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'type_code')
    # list_filter = ['type_code']
    search_fields = ['status']


admin.site.register(Appointment, AppointmentAdmin)
