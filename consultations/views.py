# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
import datetime
from braces.views import LoginRequiredMixin
from extra_views import CreateWithInlinesView, NamedFormsetsMixin
from django.utils.translation import ugettext as _
from django.contrib.messages.views import InlineSuccessMessageMixin
from .models import Consultation
from appointments.models import Appointment
from .forms import ObservationInlineFormset, ConsultationModelForm, ClinicalNotesInlineFormset
from django.http import HttpResponse


class ConsultationListView(LoginRequiredMixin, ListView):
    template_name = 'consultations/consultation_list.html'
    # friendly template context
    context_object_name = 'consultations'
    paginate_by = 50

    def get_queryset(self):
        qs = Consultation.objects.prefetch_related(
            'observation_set',
            'client',
            'patients',
            'patients__species',
            'attending_staff'
        ).all()

        return list(qs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConsultationListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['column_list'] = [
            _('Animal'),
            _('Owner'),
            _('Observation'),
            _('Time'),
            _('Vxxet'),
            _('Status')
        ]
        context['page_title'] = _('Consultations')
        context['icons'] = ['stethoscope']

        return context


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


class ConsultationCreateView(LoginRequiredMixin, NamedFormsetsMixin, InlineSuccessMessageMixin, CreateWithInlinesView):
    template_name = 'consultations/consultation_create.html'
    model = Consultation
    inlines = [ObservationInlineFormset, ClinicalNotesInlineFormset]
    # inlines_names = ['Observations', 'ClinicalNotes']
    form_class = ConsultationModelForm  # creates a custom ModelForm
    # success_url = '/appointments/'
    # success_url is ok but but Create / Update View will *automatically* use get_absolute_url() on model object

    success_message = _("Consultation was created successfully")

    def forms_valid(self, form_class, inlines):
        # form.instance.status = Appointment.STATUS_UPCOMING
        form_class.instance.start = datetime.datetime.now()
        form_class.instance.created_by = self.request.user
        form_class.instance.modified_by = self.request.user
        new_consultation = form_class.save()

        # copied from super method in ModelFormWithInlinesMixin
        for formset in inlines:
            # need to save related data e.g. Observations, before we can return it
            # as the text for Appointment 'reason'
            formset.save()

        a = Appointment(
            consultation=new_consultation,
            reason=new_consultation.observation_set.first(),
            status=Appointment.STATUS_IN_CONSULT,
            start=datetime.datetime.now(),
            client=form_class.instance.client,
            attending_staff=form_class.instance.attending_staff,
            duration=10,
            created_by=form_class.instance.created_by,
            modified_by=form_class.instance.modified_by
        )

        a.save()

        p = form_class.instance.patients
        a.patients.set([v for v in p.all()])

        # call parent form_valid to ensure other processes are completed e.g. form.save()

        # form.instance.total_leave = (self.instance.to_date - self.instance.from_date).days + 1
        # self.instance.save() //called automatically with ModelForm

        return super(ConsultationCreateView, self).forms_valid(form_class, inlines)
        # return HttpResponse(new_consultation.observation_set)
