from django.conf.urls import url

from. import views

urlpatterns = [
    url(r'^seznam/$', views.ObvestiloListView.as_view(), name="obvestilo_list"),
    url(r'^(?P<pk>\d+)/detail/$', views.ObvestiloDetailView.as_view(), name="obvestilo_detail"),

]