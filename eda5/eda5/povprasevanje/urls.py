from django.conf.urls import url


from .views import povprasevanje_views, ponudbapopostavki_views, ponudba_views, postavka_views


# HOME
urlpatterns = [
]


# Reklamacija
urlpatterns += [

    url(
        r'^povprasevanje/seznam/$', 
        povprasevanje_views.PovprasevanjeListView.as_view(), 
        name="povprasevanje_list"
    ),

    url(
        r'^(?P<pk>\d+)/detail/$', 
        povprasevanje_views.PovprasevanjeDetailView.as_view(), 
        name="povprasevanje_detail"
    ),

    url(
        r'^zunanji/(?P<pk>\d+)/detail/$', 
        povprasevanje_views.PovprasevanjeZunanjiDetailView.as_view(), 
        name="povprasevanje_zunanji_detail"
    ),

    url(
        r'^(?P<pk>\d+)/povprasevanje/create/$', 
        povprasevanje_views.PovprasevanjeCreateFromZahtevekView.as_view(), 
        name="povprasevanje_create_from_zahtevek"
    ),

    url(r'^(?P<pk>\d+)/povprasevanje/update/$', 
        povprasevanje_views.PovprasevanjeUpdateView.as_view(), 
        name="povprasevanje_update"
    ),

    url(r'^(?P<pk>\d+)/ponudba-po-postavki/update/$', 
        ponudbapopostavki_views.PonudbaPoPostavkiUpdateView.as_view(), 
        name="ponudbapopostavki_update"
    ),

    url(
        r'^(?P<pk>\d+)/ponudba-po-postavki/create/$', 
        ponudbapopostavki_views.PonudbaPoPostavkiCreateFromPovprasevanjeView.as_view(), 
        name="ponudbapopostavki_create_from_povprasevanje"
    ),

    url(
        r'^(?P<pk>\d+)/ponudba/create/$', 
        ponudba_views.PonudbaCreateFromPovprasevanjeView.as_view(), 
        name="ponudba_create_from_povprasevanje"
    ),

    url(r'^(?P<pk>\d+)/ponudba/update/$', 
        ponudba_views.PonudbaUpdateView.as_view(), 
        name="ponudba_update"
    ),

    url(
        r'^(?P<pk>\d+)/postavka/create/$', 
        postavka_views.PostavkaCreateFromPovprasevanjeView.as_view(), 
        name="postavka_create_from_povprasevanje"
    ),

    url(r'^(?P<pk>\d+)/postavka/update/$', 
        postavka_views.PostavkaUpdateView.as_view(), 
        name="postavka_update"
    ),

]