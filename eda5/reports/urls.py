from django.conf.urls import url

from .views import dn_seznam, ostalo, deli, dn_racun_dnevnik, delstavbe, obracuni_views, letno_porocilo_upravnika_views


# Racun
urlpatterns = [

]

# Strosek
urlpatterns += [
    url(r'^report_strosek/$', ostalo.ReportStrosek.as_view(), name="report_strosek"),

]

# create pdf
urlpatterns += [
    url(r'^dn-view/$', dn_seznam.dn_view, name="create_pdf_view"),
]

# print plan ov
urlpatterns += [
    url(r'^planirano-opravilo-list/$', dn_seznam.PrintPlanOVView.as_view(), name="print_plan_ov"),
]

# print plan ov
urlpatterns += [
    url(r'^deli-list-filter/$', deli.DeliSeznamPrintView.as_view(), name="print_deli_seznam_filter"),
    url(r'^prostori-list-filter/$', deli.ProstoriSeznamPrintView.as_view(), name="print_prostori_seznam_filter"),
]

# racuni in dnevniki izvedenih del
urlpatterns += [
    url(r'^dn-zbirni-dnevnik/$', dn_racun_dnevnik.DnevnikIzvedenihDelView.as_view(), name="print_dnevnik_izvedenih_del"),
]

# obracuni
urlpatterns += [
    url(r'^obracuni/zbirni-delovni-nalog/$', obracuni_views.ObracunZbirniDelovniNalogView.as_view(), name="obracuni_zbirni_delovni_nalog_view"),
    url(r'^obracuni/zbirni-delovni-nalog-planirano/$', obracuni_views.ObracunZbirniDelovniNalogPlaniranaView.as_view(), name="obracuni_zbirni_delovni_nalog_planirano_view"),
]



# Delovninalog
urlpatterns += [
    url(r'^delavci_v_delu/$', ostalo.ReportDelavciVDelu.as_view(), name="delavci_v_delu"),
    url(r'^dnevnik_izvedenih_del/$', ostalo.ReportDelovniNalogODnevnik.as_view(), name="dnevnik"),
]


# DelStavbe
urlpatterns += [

    url(
        r'^edacenter/delstavbe/zunanji(?P<pk>\d+)zunanji$',
        delstavbe.ReportDelStavbeView.as_view(),
        name="delstavbe_detail"
    ),
]

# Letno poročilo letno_porocilo_upravnika

urlpatterns += [

    url(
        r'^letno-porocilo-upravnika/porocanje-stroski/$',
        letno_porocilo_upravnika_views.PorocanjeStroskiView.as_view(),
        name="porocanje_stroski"
    ),
    url(
        r'^letno-porocilo-upravnika/porocanje-izvedena-dela/$',
        letno_porocilo_upravnika_views.PorocanjeIzvedenaDelaView.as_view(),
        name="porocanje_izvedena_dela"
    ),
]
