from django.conf.urls import url

from . import views

urlpatterns = [

    url(
        regex=r'^$',
        view=views.UvozCsv.as_view(),
        name='form'
    ),
]