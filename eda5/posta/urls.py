from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.PostaHomeView.as_view(),
        name='home'
    ),
    url(
        regex=r'^likvidacija/$',
        view=views.PostaLikvidacijaListView.as_view(),
        name='list_likvidacija'
    ),
    url(
        regex=r'^likvidirano/$',
        view=views.PostaLikvidiranListView.as_view(),
        name='list_likvidiran'
    ),
    # url(
    #     regex=r'^create/$',
    #     view=views.PostaCreateView.as_view(),
    #     name='create'
    # ),
]
