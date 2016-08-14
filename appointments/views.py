#appointments/view.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page

from .models import Appointment

class AppointmentListView(ListView):
    def get_queryset(self):
        qs = Appointment.objects.prefetch_related('client','patients')
        for r in qs:
            if r.status == r.STATUS_UPCOMING: r.css = 'default'
            if r.status == r.STATUS_ARRIVED: r.css = 'warning'
            if r.status == r.STATUS_IN_CONSULT: r.css = 'success'
            if r.status == r.STATUS_WAITING_TO_PAY: r.css = 'danger'
            if r.status == r.STATUS_PAYMENT_COMPLETE: r.css = 'info'
        return qs


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment

