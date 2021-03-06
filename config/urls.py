# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from eda5.moduli import views

urlpatterns = [
    url(r'^$', views.ModulHomeView.as_view(), name="home"),
    # url(r'^home/$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),


    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include("eda5.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^porocanje/', include("eda5.porocanjeupravnika.urls", namespace="porocanje")),

    # Your stuff: custom urls includes go here
    url(r'^moduli/', include("eda5.moduli.urls", namespace="moduli")),
    url(r'^charts/', TemplateView.as_view(template_name='line_chart.html'), name="charts"),
    # url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    # url(r'^stores/', include("eda5.stores.urls", namespace="stores")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
