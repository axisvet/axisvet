from django import forms
from .models import Consultation, Observation, Diagnosis, ClinicalNotes
from django.forms.models import inlineformset_factory
from extra_views import InlineFormSet


class ConsultationModelForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('client', 'patients', 'attending_staff')


class ObservationModelForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ('observation',)


class ClinicalNotesModelForm(forms.ModelForm):
    class Meta:
        model = ClinicalNotes
        fields = ('clinical_notes',)


class ObservationInlineFormset(InlineFormSet):
    model = Observation
    form_class = ObservationModelForm
    fields = ('observation',)
    max_num = 1
    can_delete = False
    extra = 1


class ClinicalNotesInlineFormset(InlineFormSet):
    model = ClinicalNotes
    form_class = ConsultationModelForm
    fields = ('clinical_notes',)
    max_num = 1
    can_delete = False
    extra = 1


"""
ObservationInline = inlineformset_factory(
    Consultation,
    Observation,
    fields=('observation',),
    min_num=1,
    max_num=1,
    extra=0,
    can_delete=False
)

ClinicalNotesInline = inlineformset_factory(
    Consultation,
    ClinicalNotes,
    fields=('clinical_notes',),
    min_num=1,
    max_num=1,
    extra=0,
    can_delete=False
)

DiagnosisInline = inlineformset_factory(
    Consultation,
    Diagnosis,
    fields=('diagnosis',),
    min_num=1,
    max_num=1,
    extra=0,
    can_delete=False
)
"""
