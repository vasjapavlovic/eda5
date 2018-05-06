from django.conf.urls import url

from .views import \
    dn_seznam,\
    ostalo,\
    deli,\
    dn_racun_dnevnik,\
    delstavbe,\
    obracuni_views,\
    letno_porocilo_upravnika_views,\
    racunovodstvo_reports_views,\
    delovninalogi_reports_views


urlpatterns = []

# Strosek
urlpatterns += [
    url(r'^report_strosek/$', ostalo.ReportStrosek.as_view(), name="report_strosek"),

]

# create pdf
urlpatterns += [
    url(r'^dn-view/$', dn_seznam.dn_view, name="create_pdf_view"),
]

# PLANIRANJE REPORTS
urlpatterns += [
    # (PREGLEJ ALI JE ZA IZBRISATI)
    url(
        r'^planirano-opravilo-list/$',
        dn_seznam.PrintPlanOVView.as_view(),
        name="print_plan_ov"
    ),
]


# racuni in dnevniki izvedenih del
urlpatterns += [
    url(r'^dn-zbirni-dnevnik/$', dn_racun_dnevnik.DnevnikIzvedenihDelView.as_view(), name="print_dnevnik_izvedenih_del"),
]


# DEL STAVBE REPORTS
urlpatterns += [
    # Servisna knjiga za zunanje
    url(
        r'^edacenter/delstavbe/zunanji(?P<pk>\d+)zunanji$',
        delstavbe.ReportDelStavbeView.as_view(),
        name="delstavbe_detail"
    ),
    # Deli seznam - filtrirano (PREGLEJ ALI JE ZA IZBRISATI)
    url(
        r'^deli-list-filter/$',
        deli.DeliSeznamPrintView.as_view(),
        name="print_deli_seznam_filter"
    ),
    # Prostori seznam filtrirano (PREGLEJ ALI JE ZA IZBRISATI)
    url(
        r'^prostori-list-filter/$',
        deli.ProstoriSeznamPrintView.as_view(),
        name="print_prostori_seznam_filter"
    ),
]

# LETNO POROČILO UPRAVNIKA
urlpatterns += [
    # Stroški
    url(
        r'^letno-porocilo-upravnika/porocanje-stroski/$',
        letno_porocilo_upravnika_views.PorocanjeStroskiView.as_view(),
        name="porocanje_stroski"
    ),
    # Izvedena dela
    url(
        r'^letno-porocilo-upravnika/porocanje-izvedena-dela/$',
        letno_porocilo_upravnika_views.PorocanjeIzvedenaDelaView.as_view(),
        name="porocanje_izvedena_dela"
    ),
    # Dogodki
    url(
        r'^letno-porocilo-upravnika/porocanje-dogodki/$',
        letno_porocilo_upravnika_views.PorocanjeDogodkiView.as_view(),
        name="porocanje_dogodki"
    ),
]

# RAČUNOVODSTVO REPORTS
urlpatterns += [
    # Stroški
    url(
        r'^racunovodstvo-reports/stroski/$',
        racunovodstvo_reports_views.ReportStroskiVrstaStroskaNarocilo.as_view(),
        name="racunovodstvo_reports_stroski"
    ),
]

# DELOVNINALOGI REPORTS
urlpatterns += [
    # Zbirni delovni nalog izredno
    url(
        r'^obracuni/zbirni-delovni-nalog/$',
        obracuni_views.ObracunZbirniDelovniNalogView.as_view(),
        name="obracuni_zbirni_delovni_nalog_view"
    ),
    # Zbirni delovni nalog planirano
    url(
        r'^obracuni/zbirni-delovni-nalog-planirano/$',
        obracuni_views.ObracunZbirniDelovniNalogPlaniranaView.as_view(),
        name="obracuni_zbirni_delovni_nalog_planirano_view"
    ),
    # Evidenca delovnega časa
    url(
        r'^delovnianlogi-reports/evidenca-delovnega-casa/$',
        delovninalogi_reports_views.EvidencaDelovnegaCasa.as_view(),
        name="delovninalogi_reports_evidenadelovnegacasa"
    ),
    # Delavci v delu
    url(
        r'^delavci_v_delu/$',
        ostalo.ReportDelavciVDelu.as_view(),
        name="delavci_v_delu"
    ),
]
