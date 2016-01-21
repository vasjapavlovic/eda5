from django.conf.urls import url

from . import views


# Racun
urlpatterns = [

]

# Strosek
urlpatterns += [
    url(r'^report_strosek/$', views.ReportStrosek.as_view(), name="report_strosek"),

]
