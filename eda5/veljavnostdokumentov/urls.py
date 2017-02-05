from django.conf.urls import url

from .views import VeljavnostDokumentaCreateView, VeljavnostDokumentaUpdateView


# veljavnost dokumentov
urlpatterns = [
    url(r'^veljavnost-dokumenta-create/(?P<pk>\d+)$', VeljavnostDokumentaCreateView.as_view(), name="veljavnost_dokumenta_create"),
    url(r'^(?P<pk>\d+)/veljavnost-dokumenta-update/$', VeljavnostDokumentaUpdateView.as_view(), name="veljavnost_dokumenta_update"),
]