# visitors/view.py

from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from .models import Client
from .models import Patient

# ======================= #
# ====== clients========= #
# ======================= #


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'visitors/client_list.html'
    # friendly template context
    context_object_name = 'clients'
    paginate_by = 50

    def get_queryset(self):
        # form = form_class(self.request.GET)
        q = self.request.GET.get("q")
        if q:
            qs = Client.objects.prefetch_related(
                'patients',
                'patients__species'
            ).all().distinct()

        else:
            qs = Client.objects.prefetch_related(
                'patients',
                'patients__species'
            ).all().distinct()

        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['column_list'] = [
            _('Name'),
            _('Patient'),
            _('Street Address'),
            _('Mobile'),
            _('XXX'),
            _('XXX')
        ]

        context['page_title'] = _('Clients')
        context['icons'] = ['group']
        context['add_url'] = reverse('visitors:client_create')
        context['include_search'] = True
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('first_name',)
    template_name = 'visitors/client_create.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['page_title'] = _('New client')
        context['icons'] = ['group']
        context['add_url'] = ''
        context['include_search'] = False
        return context


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client


# ======================= #
# ====== patients ======= #
# ======================= #

class PatientListView(LoginRequiredMixin, ListView):
    template_name = 'visitors/patient_list.html'
    # friendly template context
    context_object_name = 'patients'
    paginate_by = 50

    def get_queryset(self):

        q = self.request.GET.get("q")

        if q:
            qs = Patient.objects.filter(name__icontains=q).select_related(
                'species',
                'client'
            ).distinct()

        else:
            qs = Patient.objects.select_related(
                'species',
                'client'
            ).distinct()

        return list(qs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['column_list'] = [
            _('Species'),
            _('Name'),
            _('Weight (kg)'),
            _('Breed'),
            _('Owner'),
            _('XXX'),
        ]
        context['page_title'] = _('Patients')
        context['icons'] = ['dog', 'cat', 'rabbit']
        context['add_url'] = reverse('visitors:patient_create')
        context['include_search'] = True
        return context


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context['page_title'] = _('New patient')
        context['icons'] = ['dog', 'cat', 'rabbit']
        context['add_url'] = ''
        context['include_search'] = False
        return context


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
