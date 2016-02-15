from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
    # url(r'^$', views.PartnerHomeView.as_view(), name='home'),
]

# LastniskaEnotaInterna
urlpatterns += [
    url(r'^interna-list-teh/$', views.LastniskaEnotaInternaListTehView.as_view(), name='int_list_teh'),
    url(r'^interna-list-last/$', views.LastniskaEnotaInternaListLastView.as_view(), name='int_list_last'),
    url(r'^(?P<pk>\d+)/interna-detail/$', views.LastniskaEnotaInternaDetailView.as_view(), name='int_detail'),
]
