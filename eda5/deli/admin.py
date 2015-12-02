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


class DelStavbeInlines(admin.TabularInline):
    model = models.DelStavbe
    extra = 0


class PodskupinaDelovInlines(admin.TabularInline):
    model = models.Podskupina
    extra = 0


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
    list_display = ("oznaka", "naziv", "lastniska_skupina", "podskupina")
    # dodati še lastniško skupino
    ordering = ["oznaka"]
    search_fields = ["oznaka", ]
    # readonly_fields = ["stevilka",]
    inlines = [
        ProjektnoMestoInlines,
    ]


@admin.register(models.ProjektnoMesto)
class ProjektnoMestoAdmin(admin.ModelAdmin):
    inlines = [
        ElementInlines,

    ]
    ordering = [
        "del_stavbe__oznaka", 
        "oznaka",
    ]


@admin.register(models.Element)
class ElementAdmin(admin.ModelAdmin):
    inlines = [
        PlaniranaAktivnostInline,
    ]