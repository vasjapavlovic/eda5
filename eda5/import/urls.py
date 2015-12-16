from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.UvozCsv.as_view(), name='form'),
]
