from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.RazdelilnikHomeView.as_view(), name="home"),

]