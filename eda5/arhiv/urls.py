from django.conf.urls import url

from .views import ArhiviranjePopUpListView


# HOME
urlpatterns = [
]

# Arhiviranje
urlpatterns += [
    url(r'^arhiviranje/popup-list/?$', ArhiviranjePopUpListView.as_view(), name='arhiviranje_popup_list'),
]




