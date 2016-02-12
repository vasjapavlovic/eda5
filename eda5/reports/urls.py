from django.conf.urls import url

from . import views


# Racun
urlpatterns = [

]

# Strosek
urlpatterns += [
    url(r'^report_strosek/$', views.ReportStrosek.as_view(), name="report_strosek"),

]

# create pdf
urlpatterns += [
    url(r'^create_pdf/$', views.create_pdf_view, name="create_pdf_view"),
]