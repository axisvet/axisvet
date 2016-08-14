#appointments/view.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse

from .models import Appointment

class AppointmentListView(LoginRequiredMixin, ListView):
    #model = Appointment
    queryset = Appointment.objects.prefetch_related('client','patients')


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment

