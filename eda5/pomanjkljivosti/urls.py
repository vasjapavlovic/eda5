from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PomanjkljivostiHomeView.as_view(), name="home")
]

# POMANJKLJIVOST
urlpatterns += [
    url(r'^create/$', views.PomanjkljivostCreateView.as_view(), name="pomanjkljivost_create"),
    url(r'^seznam/$', views.PomanjkljivostListView.as_view(), name="pomanjkljivost_list"),
    url(r'^(?P<pk>\d+)/detail/$', views.PomanjkljivostDetailView.as_view(), name="pomanjkljivost_detail"),
]
