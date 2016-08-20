# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from braces.views import LoginRequiredMixin
from .models import Appointment
from .forms import AppointmentForm


class AppointmentListView(LoginRequiredMixin, ListView):
    template_name = 'appointments/appointment_list.html'
    # friendly template context
    context_object_name = 'appointments'
    paginate_by = 50

    def get_queryset(self):
        qs = Appointment.objects.prefetch_related('client', 'patients',
                                                  'patients__species', 'attending_staff__appointment_set')

        return list(qs)


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment


class AppointmentUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Appointment


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_create.html'
