from django.contrib import admin

from . import models


class PlanOVInline(admin.TabularInline):
    model = models.PlanOV
    extra = 0


class ProizvajalecAdmin(admin.ModelAdmin):

    class Meta:
        model = models.Proizvajalec


class TipArtiklaAdmin(admin.ModelAdmin):

    class Meta:
        model = models.TipArtikla


class ModelArtiklaAdmin(admin.ModelAdmin):

    inlines = [PlanOVInline,
               ]
    filter_horizontal = ('dokumentacija',)

    class Meta:
        model = models.ModelArtikla


class PlanOVAdmin(admin.ModelAdmin):

    class Meta:
        model = models.PlanOV


class RezevniDelAdmin(admin.ModelAdmin):

    class Meta:
        model = models.RezervniDel

admin.site.register(models.Proizvajalec, ProizvajalecAdmin)
admin.site.register(models.TipArtikla, TipArtiklaAdmin)
admin.site.register(models.ModelArtikla, ModelArtiklaAdmin)
admin.site.register(models.PlanOV, PlanOVAdmin)
admin.site.register(models.RezervniDel, RezevniDelAdmin)
