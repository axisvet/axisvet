# appointments/view.py
from django.views.generic import ListView, DetailView, UpdateView, CreateView
import datetime
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from extra_views import CreateWithInlinesView, NamedFormsetsMixin, UpdateWithInlinesView
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
    paginate_by = 25

    def get_queryset(self):
        qs = Consultation.objects.prefetch_related(
            'observation_set',
            'patients',
            'patients__species',
        ).select_related('client', 'attending_staff').all().order_by('start')
        return list(qs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConsultationListView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['decorator_text'] = Consultation._meta.verbose_name_plural
        context['icons'] = Consultation.PAGE_ICONS
        context['url'] = reverse('consultations:create')
        return context


class ConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Consultation

    def get_queryset(self):
        qs = Consultation.objects.select_related(
            'attending_staff',
            'created_by',
            'modified_by',
            'client',
        ).prefetch_related('patients', 'observation_set')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConsultationDetailView, self).get_context_data(**kwargs)
        # Define required column headers in listview template
        context['decorator_text'] = Consultation._meta.verbose_name + ' ' + _('details')
        context['icons'] = Consultation.PAGE_ICONS
        return context


class ConsultationCreateView(LoginRequiredMixin, NamedFormsetsMixin, InlineSuccessMessageMixin, CreateWithInlinesView):
    template_name = 'consultations/consultation_create.html'
    model = Consultation
    inlines = [ObservationInlineFormset, ClinicalNotesInlineFormset]
    form_class = ConsultationModelForm  # creates a custom ModelForm
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConsultationCreateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Add') + ' ' + Consultation._meta.verbose_name
        context['icons'] = Consultation.PAGE_ICONS
        return context


class ConsultationUpdateView(LoginRequiredMixin, NamedFormsetsMixin, InlineSuccessMessageMixin, UpdateWithInlinesView):

    template_name = 'consultations/consultation_create.html'
    model = Consultation
    inlines = [ObservationInlineFormset, ClinicalNotesInlineFormset]
    form_class = ConsultationModelForm  # creates a custom ModelForm
    success_message = _("Consultation was updated successfully")

    def forms_valid(self, form_class, inlines):
        # form.instance.status = Appointment.STATUS_UPCOMING ##don't change
        form_class.instance.start = datetime.datetime.now()
        # form_class.instance.created_by = self.request.user ##don't change
        form_class.instance.modified_by = self.request.user
        new_consultation = form_class.save()

        # copied from super method in ModelFormWithInlinesMixin
        for formset in inlines:
            # need to save related data e.g. Observations, before we can return it
            # as the text for Appointment 'reason'
            formset.save()
        # #do not touch appointment
        """
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
        """

        # call parent form_valid to ensure other processes are completed e.g. form.save()

        # form.instance.total_leave = (self.instance.to_date - self.instance.from_date).days + 1
        # self.instance.save() //called automatically with ModelForm

        return super(ConsultationUpdateView, self).forms_valid(form_class, inlines)
        # return HttpResponse(new_consultation.observation_set)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConsultationUpdateView, self).get_context_data(**kwargs)
        context['decorator_text'] = _('Update') + ' ' + Consultation._meta.verbose_name
        context['icons'] = Consultation.PAGE_ICONS
        return context
