from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('reason', 'status', 'start', 'duration', 'attending_staff', 'client', 'patients')
