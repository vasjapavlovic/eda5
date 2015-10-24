from django.conf.urls import include, url

from .views import ModulListView

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=ModulListView.as_view(),
        name="list"
    ),

    url(
        regex=r'^stores/',
        view=include("eda5.stores.urls", namespace="stores"),
    ),
]