def nav_bar_alerts(request):
    from appointments.models import Appointment
    qs = Appointment.objects.filter(status=Appointment.STATUS_WAITING_TO_PAY).count()
    return{'TO_PAY_COUNT': qs}
