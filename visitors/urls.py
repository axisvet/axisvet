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

    # ======= patients =======
    url(
        regex=r'^clients/$',
        view=views.ClientListView.as_view(),
        name='client_list'
    ),
    url(
        regex=r'^clients/(?P<pk>\d+)/$',
        view=views.ClientDetailView.as_view(),
        name='client_detail'
    ),
    url(
        regex=r'^clients/(?P<pk>\d+)/update/$',
        view=views.ClientUpdateView.as_view(),
        name='client_update'
    ),
    url(
        regex=r'^clients/new/$',
        view=views.ClientCreateView.as_view(),
        name='client_create'
    ),


    # ======= patients =======
    url(
        regex=r'^patients/$',
        view=views.PatientListView.as_view(),
        name='patient_list'
    ),
    url(
        regex=r'^patients/(?P<pk>\d+)/$',
        view=views.PatientDetailView.as_view(),
        name='patient_detail'
    ),
    url(
        regex=r'^patients/(?P<pk>\d+)/update/$',
        view=views.PatientUpdateView.as_view(),
        name='patient_update'
    ),
    url(
        regex=r'^patients/new/$',
        view=views.PatientCreateView.as_view(),
        name='patient_create'
    ),

]
