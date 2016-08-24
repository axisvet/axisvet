from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ConsultationListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.ConsultationDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.ConsultationUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^new/$',
        view=views.ConsultationCreateView.as_view(),
        name='create'
    ),
]
