from django.conf.urls import url

from .views import dn_seznam, ostalo, deli


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
    url(r'^planirano-opravilo-list/$', dn_seznam.PrintPlanOVView, name="print_plan_ov"),
]

# print plan ov
urlpatterns += [
    url(r'^deli-list-filter/$', deli.DeliSeznamPrintView, name="print_deli_seznam_filter"),
]





# Delovninalog
urlpatterns += [
    url(r'^delavci_v_delu/$', ostalo.ReportDelavciVDelu.as_view(), name="delavci_v_delu"),
    url(r'^dnevnik_izvedenih_del/$', ostalo.ReportDelovniNalogODnevnik.as_view(), name="dnevnik"),
]