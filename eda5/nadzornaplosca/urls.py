from django.conf.urls import url

from . import views


# nadzorne enote
urlpatterns = [
    url(r'^nadzorni-sistem-seznam/$', views.NadzorniSistemListView.as_view(), name="nadzorni_sistem_list"),
]
