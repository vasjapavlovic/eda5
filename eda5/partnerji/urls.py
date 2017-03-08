from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
    url(r'^$', views.PartnerHomeView.as_view(), name='home'),
]

# Partner
urlpatterns += [
    url(r'^seznam/$', views.PartnerListView.as_view(), name='partner_list'),
    url(r'^(?P<pk>\d+)/detail/$', views.PartnerDetailView.as_view(), name='partner_detail'),
    url(r'^create/$', views.PartnerCreateView.as_view(), name='partner_create'),
    url(r'^(?P<pk>\d+)/update/$', views.PartnerUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/update-komplet/$', views.PartnerUpdateKompletView.as_view(), name='partner_update_komplet'),
    # POP UP VIEWS
    url(r'^partner/popup-create/?$', views.PartnerPopupCreateView.as_view(), name='partner_popup_create'),
    url(r'^partner/popup-list/?$', views.PartnerPopUpListView.as_view(), name='partner_popup_list'),




]

# Oseba
urlpatterns += [
    url(r'^oseba_create/$', views.OsebaCreateView.as_view(), name='oseba_create'),
]
