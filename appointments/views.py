# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import LoginRequiredMixin
from extra_views import SearchableListMixin
from .models import Appointment
from .forms import AppointmentForm


class AppointmentListView(LoginRequiredMixin, SearchableListMixin, ListView):
    template_name = 'appointments/appointment_list.html'
    # friendly template context
    context_object_name = 'appointments'
    paginate_by = 50

    queryset = Appointment.objects.select_related('client', 'attending_staff').prefetch_related(
            'patients',
            'patients__species',
            )

    search_fields = ['status', 'start', 'reason', 'client__first_name', 'client__last_name',
                     'client__street_address', 'client__ifomobile', 'patients__name', 'patients__species__name']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        context['decorator_text'] = Appointment._meta.verbose_name_plural
        context['icons'] = Appointment.PAGE_ICONS
        context['url'] = reverse('appointments:create')
        return context


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppointmentDetailView, self).get_context_data(**kwargs)
        context['decorator_text'] = Appointment._meta.verbose_name + ' ' + _('details')
        context['icons'] = Appointment.PAGE_ICONS
        return context


class AppointmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_create.html'
    success_message = _("Appointment '%(reason)s' on %(start)s was created successfully")

    def form_valid(self, form):
        form.instance.status = Appointment.STATUS_UPCOMING
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Add') + ' ' + Appointment._meta.verbose_name
        context['icons'] = Appointment.PAGE_ICONS
        return context


class AppointmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_create.html'
    success_message = _("Appointment was update successfully")

    def form_valid(self, form):
        # form.instance.status = Appointment.STATUS_UPCOMING
        # form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AppointmentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Update') + ' ' + Appointment._meta.verbose_name
        context['icons'] = Appointment.PAGE_ICONS
        return context
