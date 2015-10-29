from django.conf.urls import include, url

from .views import ModulListView

urlpatterns = [
    # registracija MODULOV (urlji)
    url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    url(r'^posta/', include("eda5.posta.urls", namespace="posta")),
    url(r'^racunovodstvo/', include("eda5.racunovodstvo.urls", namespace="racunovodstvo")),
    url(r'^razdelilnik/', include("eda5.razdelilnik.urls", namespace="razdelilnik")),
    url(r'^stores/', include("eda5.stores.urls", namespace="stores")),
]

# Glavni URL za modul
urlpatterns += [
    url(r'^$', ModulListView.as_view(), name="list"),
]
