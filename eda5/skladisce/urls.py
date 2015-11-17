from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
    url(r'^$', views.SkladisceHomeView.as_view(), name="home"),
]

# DOBAVA
urlpatterns += [
    url(r'^dobava/seznam/$', views.DobavaListView.as_view(), name="dobava_list"),
    url(r'^dobava/create/$', views.DobavaCreateView.as_view(), name="dobava_create"),
]
