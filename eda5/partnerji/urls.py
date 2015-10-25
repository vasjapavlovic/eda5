from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.PartnerListView.as_view(),
        name='list'
    ),
]
