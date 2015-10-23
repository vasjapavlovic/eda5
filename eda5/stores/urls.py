from django.conf.urls import url

from .views import IceCreamStoreListView
from .views import IceCreamStoreDetailView
from .views import IceCreamStoreCreateView
from .views import IceCreamStoreUpdateView

urlpatterns = [
    url(r'^$', IceCreamStoreListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/detail/$', IceCreamStoreDetailView.as_view(), name="detail"),
    url(r'^create/$', IceCreamStoreCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/update/$', IceCreamStoreUpdateView.as_view(), name="update"),
]