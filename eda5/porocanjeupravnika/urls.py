from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/user/detail/$', views.PorocanjeUpravnikaDetailView.as_view(), name="user_detail"),
]
