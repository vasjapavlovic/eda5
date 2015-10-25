from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.PartnerHomeView.as_view(),
        name='home'
    ),

    url(
        regex=r'^seznam/$',
        view=views.PartnerListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^(?P<pk>\d+)/detail/$',
        view=views.PartnerDetailView.as_view(),
        name='detail'
    ),

    url(
        regex=r'^create/$',
        view=views.PartnerCreateView.as_view(),
        name='create'
    ),

    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.PartnerUpdateView.as_view(),
        name='update'
    ),
]
