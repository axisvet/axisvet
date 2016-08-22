# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import LoginRequiredMixin
from .models import Appointment
from .forms import AppointmentForm


class AppointmentListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'appointments/appointment_list.html'
    # friendly template context
    context_object_name = 'appointments'
    paginate_by = 50

    def get_queryset(self):
        qs = Appointment.objects.prefetch_related(
            'client',
            'patients',
            'patients__species',
            'attending_staff__appointment_set')

        return list(qs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppointmentListView, self).get_context_data(**kwargs)

        # Define required column headers in listview template
        context['column_list'] = [

            _('Animal'),
            _('Owner'),
            _('Reason'),
            _('Time'),
            _('Vet'),
            _('Status')
        ]
        context['page_title'] = _('Appointments')
        context['icons'] = ['calendar']
        return context


class AppointmentDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Appointment


class AppointmentUpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Appointment


class AppointmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_create.html'
    # success_url = '/appointments/'
    success_message = _("Appointment '%(reason)s' on %(start)s was created successfully")

    def form_valid(self, form):
        form.instance.status = Appointment.STATUS_UPCOMING
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)
