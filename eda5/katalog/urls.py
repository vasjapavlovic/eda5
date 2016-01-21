from django.conf.urls import url

from . import views



# HOME
urlpatterns = [

]


# Proizvajalec
urlpatterns += [
    url(r'^proizvajalec-list/$', views.ProizvajalecListView.as_view(), name="proizvajalec_list"),

]


# TipArtikla
urlpatterns += [
    url(r'^tip-artikla-list/$', views.TipArtiklaListView.as_view(), name="tip_artikla_list"),

]


# ModelArtikla
urlpatterns += [
    url(r'^model-artikla-list/$', views.ModelArtiklaListView.as_view(), name="model_artikla_list"),

]
