from django.contrib import admin

from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela


@admin.register(Zahtevek)
class ZahtevekAdmin(admin.ModelAdmin):
    pass


@admin.register(ZahtevekSkodniDogodek)
class ZahtevekSkodniDogodekAdmin(admin.ModelAdmin):
    filter_horizontal = ("poskodovane_stvari",)


@admin.register(ZahtevekSestanek)
class ZahtevekSestanekAdmin(admin.ModelAdmin):
    filter_horizontal = ("udelezenci",)


@admin.register(ZahtevekIzvedbaDela)
class ZahtevekIzvedbaDelaAdmin(admin.ModelAdmin):
    pass
