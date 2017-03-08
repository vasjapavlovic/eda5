from django.conf.urls import url

# importamo komplet views
from .views import obrazec_splosno_views



urlpatterns = [
]

urlpatterns += [
	
	url(r'^dopis/create/$', 
        obrazec_splosno_views.DopisCreateView.as_view(), 
        name="dopis_create"),


	url(r'^dopis/list/$', 
        obrazec_splosno_views.DopisListView.as_view(), 
        name="dopis_list"),


    url(r'^(?P<pk>\d+)/dopis-detail/$', 
        obrazec_splosno_views.DopisDetailView.as_view(), 
        name="dopis_detail"),

]