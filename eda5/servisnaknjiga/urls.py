from django.conf.urls import url

# importamo komplet views
from .views import ParameterDetailView



urlpatterns = [
]

urlpatterns += [



    url(r'^parameter/(?P<pk>\d+)/detail/$',
        ParameterDetailView.as_view(),
        name="parameter_detail"),
]
