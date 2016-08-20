# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from braces.views import LoginRequiredMixin
from .models import Consultation
from .forms import ConsultationForm


class ConsultationListView(LoginRequiredMixin, ListView):
    template_name = 'consultations/consultation_list.html'
    # friendly template context
    context_object_name = 'consultations'
    paginate_by = 50

    def get_queryset(self):
        #qs = Consultation.objects.prefetch_related('client', 'patients')
        qs=''
        return list(qs)


class ConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Consultation


class ConsultationUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Consultation


class ConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultations/consultation_create.html'
