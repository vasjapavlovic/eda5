from django.conf.urls import url

from .views import dn_seznam, ostalo, deli, dn_racun_dnevnik, delstavbe


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