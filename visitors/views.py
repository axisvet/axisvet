# visitors/view.py

from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView, CreateView
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
            qs = Client.objects.prefetch_related('patients', 'patients__species').all().distinct()
        else:
            qs = Client.objects.prefetch_related('patients', 'patients__species').all().distinct()

        return qs


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client


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
            qs = Patient.objects.filter(name__icontains=q).select_related('species', 'client').distinct()
        else:
            qs = Patient.objects.select_related('species', 'client').distinct()

        return list(qs)


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
