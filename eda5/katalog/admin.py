from django.contrib import admin

from . import models


class ArtikelPlanInline(admin.TabularInline):
    model = models.ArtikelPlan
    extra = 0


class ModelArtiklaInline(admin.TabularInline):
    model = models.ModelArtikla
    extra = 0


class ObratovalniParameterInline(admin.TabularInline):
    model = models.ObratovalniParameter
    extra = 0


class ProizvajalecAdmin(admin.ModelAdmin):

    inlines = [
        ModelArtiklaInline,
    ]

    class Meta:
        model = models.Proizvajalec


class TipArtiklaAdmin(admin.ModelAdmin):

    class Meta:
        model = models.TipArtikla


class ModelArtiklaAdmin(admin.ModelAdmin):

    inlines = [
        ArtikelPlanInline,
        ObratovalniParameterInline,
    ]

    ordering = [
        'proizvajalec__naziv'
    ]

    class Meta:
        model = models.ModelArtikla


class ArtikelPlanAdmin(admin.ModelAdmin):

    class Meta:
        model = models.ArtikelPlan


class RezevniDelAdmin(admin.ModelAdmin):

    class Meta:
        model = models.RezervniDel


@admin.register(models.ObratovalniParameter)
class ObratovalniParameterAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Proizvajalec, ProizvajalecAdmin)
admin.site.register(models.TipArtikla, TipArtiklaAdmin)
admin.site.register(models.ModelArtikla, ModelArtiklaAdmin)
admin.site.register(models.ArtikelPlan, ArtikelPlanAdmin)
admin.site.register(models.RezervniDel, RezevniDelAdmin)
