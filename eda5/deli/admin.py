from django.contrib import admin

from . import models
from eda5.planiranje.admin import PlaniranaAktivnostInline
# from .forms import ModelArtiklaAdminForm


class ElementInlines(admin.TabularInline):
    model = models.Element
    extra = 0


class ProjektnoMestoInlines(admin.TabularInline):
    model = models.ProjektnoMesto
    extra = 0
    raw_id_fields = ("lokacija",)


class DelStavbeInlines(admin.TabularInline):
    model = models.DelStavbe
    extra = 0


class PodskupinaDelovInlines(admin.TabularInline):
    model = models.Podskupina
    extra = 0


class NastavitevInlines(admin.TabularInline):
    model = models.Nastavitev
    extra = 0



@admin.register(models.Stavba)
class StavbaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Etaza)
class EtazaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lokacija)
class LokacijaAdmin(admin.ModelAdmin):
    pass



@admin.register(models.Skupina)
class SkupinaAdmin(admin.ModelAdmin):
    list_display = ("oznaka", "naziv")
    search_fields = ["naziv", ]
    ordering = ["oznaka"]
    # readonly_fields = ["stevilka",]
    inlines = [
        PodskupinaDelovInlines,
    ]


@admin.register(models.Podskupina)
class PodskupinaAdmin(admin.ModelAdmin):
    list_display = ("oznaka", "naziv")
    search_fields = ["naziv", ]
    ordering = ["oznaka"]
    # readonly_fields = ["stevilka",]
    inlines = [
        DelStavbeInlines,
    ]


@admin.register(models.DelStavbe)
class DelStavbeAdmin(admin.ModelAdmin):
    list_display = (
        "oznaka", 
        "naziv", 
        'funkcija',
        "lastniska_skupina", 
        "podskupina"
    )
    # dodati še lastniško skupino
    ordering = ["oznaka"]
    search_fields = ["oznaka", "naziv" ]
    # readonly_fields = ["stevilka",]
    inlines = [
        ProjektnoMestoInlines,
    ]


@admin.register(models.ProjektnoMesto)
class ProjektnoMestoAdmin(admin.ModelAdmin):
    list_display = (
        'oznaka',
        'naziv',
        'funkcija',
        'bim_id',
        'tip_elementa',
        'lokacija',
        'del_stavbe',
    )
    search_fields = ["oznaka", "naziv" ]
    inlines = [
        ElementInlines,

    ]
    ordering = [
        "del_stavbe__oznaka", 
        "oznaka",
    ]
    raw_id_fields = ("lokacija", "del_stavbe")


@admin.register(models.Element)
class ElementAdmin(admin.ModelAdmin):
    inlines = [
        PlaniranaAktivnostInline,
        NastavitevInlines,
    ]


@admin.register(models.Nastavitev)
class NastavitevAdmin(admin.ModelAdmin):
    pass