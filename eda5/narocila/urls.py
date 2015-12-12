from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.NarocilaHomeView.as_view(), name="home"),
]


# DELOVNI NALOG
# urlpatterns += [
#     url(r'^dn/$', views.DelovniNalogList.as_view(), name="dn_list"),
# ]
