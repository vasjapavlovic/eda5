from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PostaHomeView.as_view(), name="home"),
    url(r'^dokument/popup-list/?$', views.DokumentPopUpListView.as_view(), name='dokument_popup_list'),
]

# DOKUMENT
urlpatterns += [
    url(r'^seznam/?$', views.DokumentListView.as_view(), name="dokument_list"),
    url(r'^seznam-filter/?$', views.DokumentCustomListView.as_view(), name="dokument_list_filtered"),
    url(r'^create/$', views.DokumentCreateView.as_view(), name="dokument_create"),
    url(r'^(?P<pk>\d+)/update-from-partner/$', views.DokumentUpdateFromPartnerView.as_view(), name="dokument_from_partner_update"),
    url(r'^(?P<pk>\d+)/update/$', views.DokumentUpdateView.as_view(), name="dokument_update"),
    url(r'^reload_controls.html$', views.reload_controls_view, name='reload_controls'),
    url(r'^(?P<pk>\d+)/detail/$', views.PostaDokumentDetailView.as_view(), name="dokument_detail"),
]
