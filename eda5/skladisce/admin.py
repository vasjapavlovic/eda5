from django.contrib import admin

from .models import Dobava, Artikel, TipArtikla, SklopArtikla, Dnevnik


@admin.register(Dobava)
class DobavaAdmin(admin.ModelAdmin):
    pass


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    pass


@admin.register(TipArtikla)
class TipArtiklaAdmin(admin.ModelAdmin):
    pass


@admin.register(SklopArtikla)
class SklopArtiklaAdmin(admin.ModelAdmin):
    pass


@admin.register(Dnevnik)
class DnevnikAdmin(admin.ModelAdmin):
    pass
