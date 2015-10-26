from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.RacunovodstvoHomeView.as_view(),
        name='home'
    ),
]