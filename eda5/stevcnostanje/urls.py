from django.conf.urls import url

from. import views

urlpatterns = [
    url(r'^$', views.StevciHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.DelilnikListView.as_view(), name="delilnik_list"),
    url(r'^(?P<pk>\d+)/detail/$', views.DelilnikDetailView.as_view(), name="delilnik_detail"),

]