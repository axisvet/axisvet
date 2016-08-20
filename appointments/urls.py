# appointments/url.py

# when a pattern matches, Django imports and calls the given view, which receives HttpRequests + args in "()"
# request /articles/2005/03/ would be parsed by
# url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive) and the two sets of "()" in regex means
# means the values are captured and passed onto view... so call is views.month_archive(request, '2005', '03')
# if no brackets then no variables are passed e.g. /articles/2003/ request sent to
# url(r'^articles/2003/$', views.special_case_2003) would just call function views.special_case_2003(request)

# if we want the args named (not just positional) we can use (?P<year>[0-9]{4}) instead of ([0-9]{4})
# so we get views.month_archive(request, year='2005', month='03') instead of views.month_archive(request, '2005', '03')

# a third argument is also allowed: url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
# if url is /blog/2005/ this would call function views.year_archive(request, year='2005', foo='bar')


from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.AppointmentListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.AppointmentDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^updatestatus/(?P<pk>\d+)/$',
        view=views.AppointmentUpdateStatusView.as_view(),
        name='update_status'
    ),
    url(
        regex=r'^new/$',
        view=views.AppointmentCreateView.as_view(),
        name='create'
    ),

]
