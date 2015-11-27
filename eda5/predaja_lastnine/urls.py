from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PredajaLastnineHomeView.as_view(), name="home"),
]

# PredajaLastnine
urlpatterns += [
    url(r'^predaja/list$', views.PredajaListView.as_view(), name="predaja_list"),
    url(r'^predaja/create$', views.PredajaCreateView.as_view(), name="predaja_create"),
]

