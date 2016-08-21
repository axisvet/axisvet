# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
import datetime
from braces.views import LoginRequiredMixin
from extra_views import CreateWithInlinesView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import InlineSuccessMessageMixin
from .models import Consultation
from .forms import ObservationInlineFormset, ConsultationModelForm, ClinicalNotesInlineFormset


class ConsultationListView(LoginRequiredMixin, ListView):
    template_name = 'consultations/consultation_list.html'
    # friendly template context
    context_object_name = 'consultations'
    paginate_by = 50

    def get_queryset(self):
        qs = Consultation.objects.all()
        return list(qs)


class ConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Consultation


class ConsultationUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Consultation


"""
class ConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultations/consultation_create.html'
    success_url = '/consultations/'
    success_message = _("Consultation started successfully")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(ConsultationCreateView, self).form_valid(form)
"""


class ConsultationCreateView(LoginRequiredMixin, InlineSuccessMessageMixin, CreateWithInlinesView):
    template_name = 'consultations/consultation_create.html'
    model = Consultation
    inlines = [ObservationInlineFormset, ClinicalNotesInlineFormset]
    form_class = ConsultationModelForm
    success_url = '/appointments/'
    success_message = _("Consultation was created successfully")

    def forms_valid(self, form_class, inlines):
        # form.instance.status = Appointment.STATUS_UPCOMING
        form_class.instance.start = datetime.datetime.now()
        form_class.instance.created_by = self.request.user
        form_class.instance.modified_by = self.request.user

        return super(ConsultationCreateView, self).forms_valid(form_class, inlines)
