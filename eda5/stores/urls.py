# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.IceCreamStoreListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^create/$',
        view=views.IceCreamStoreCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<pk>\d+)/detail/$',
        view=views.IceCreamStoreDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.IceCreamStoreUpdateView.as_view(),
        name='update'
    ),
]
