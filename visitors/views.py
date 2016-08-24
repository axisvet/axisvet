# visitors/view.py
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from extra_views import SearchableListMixin
from .models import Client
from .models import Patient

# ======================= #
# ====== clients========= #
# ======================= #


class ClientListView(LoginRequiredMixin, SearchableListMixin, ListView):
    template_name = 'visitors/client_list.html'
    # friendly template context
    context_object_name = 'clients'
    paginate_by = 50
    queryset = Client.objects.prefetch_related('patients', 'patients__species').all().distinct()
    search_fields = ['first_name', 'last_name', 'email',
                     'street_address', 'mobile', 'patients__name', 'patients__species__name']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['decorator_text'] = Client._meta.verbose_name_plural
        context['icons'] = Client.PAGE_ICONS
        context['url'] = reverse('visitors:client_create')
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['decorator_text'] = Client._meta.verbose_name + ' ' + _('details')
        context['icons'] = Client.PAGE_ICONS
        return context


class ClientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Client
    fields = (
        'first_name',
        'last_name',
        'email',
        'street_address',
        'street_address_2',
        'city',
        'zip',
        'county',
        'mobile',
        'organisation_name',
    )
    template_name = 'visitors/client_patient_create_update.html'
    success_message = _("Client %(first_name)s %(last_name)s was added successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Add') + ' ' + Client._meta.verbose_name
        context['icons'] = Client.PAGE_ICONS
        return context


class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client

    fields = (
        'first_name',
        'last_name',
        'email',
        'street_address',
        'street_address_2',
        'city',
        'zip',
        'county',
        'mobile',
        'organisation_name',
    )

    template_name = 'visitors/client_patient_create_update.html'
    success_message = _("Client was updated successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Update') + ' ' + Client._meta.verbose_name
        context['icons'] = Client.PAGE_ICONS
        return context

# ======================= #
# ====== patients ======= #
# ======================= #


class PatientListView(LoginRequiredMixin, SearchableListMixin, ListView):
    template_name = 'visitors/patient_list.html'
    # friendly template context
    context_object_name = 'patients'
    paginate_by = 50
    queryset = Patient.objects.select_related('client', 'species').distinct().order_by('name')
    search_fields = ['species__name', 'breed', 'name', 'client__first_name', 'client__last_name']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['decorator_text'] = Patient._meta.verbose_name_plural
        context['icons'] = Patient.PAGE_ICONS
        context['url'] = reverse('visitors:patient_create')
        return context


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['decorator_text'] = Patient._meta.verbose_name + ' ' + _('details')
        context['icons'] = Patient.PAGE_ICONS
        return context


class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = (
        'species',
        'breed',
        'gender',
        'name',
        'client',
        'weight',
        'date_of_birth',
        'colour',
        'remarks',
        'microchip',
    )
    template_name = 'visitors/client_patient_create_update.html'
    success_message = _("Patient %(name)s was added successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Add') + ' ' + Patient._meta.verbose_name
        context['icons'] = Patient.PAGE_ICONS
        return context


class PatientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    fields = (
        'species',
        'breed',
        'gender',
        'name',
        'client',
        'weight',
        'date_of_birth',
        'colour',
        'remarks',
        'microchip',
    )
    template_name = 'visitors/client_patient_create_update.html'
    success_message = _("Patient %(name)s was updated successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientUpdateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Update') + ' ' + Patient._meta.verbose_name
        context['icons'] = Patient.PAGE_ICONS
        return context
