from django.conf.urls import url


from .views.PredajaLastnine import PredajaLastnineListView

# HOME
urlpatterns = [
]


# Predaja Lastnine
urlpatterns += [
    url(r'^predaja-lastnine-list/$', PredajaLastnineListView.as_view(), name="predajalastnine_list"),

]