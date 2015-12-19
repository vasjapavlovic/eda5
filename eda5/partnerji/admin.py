from django.contrib import admin


from . import models


@admin.register(models.SkupinaPartnerjev)
class SkupinaAdmin(admin.ModelAdmin):
    filter_horizontal = ['partner']
    search_fields = ('naziv',)

@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):

    search_fields = ('kratko_ime',)

admin.site.register(models.Drzava)
admin.site.register(models.Posta)
admin.site.register(models.Banka)
admin.site.register(models.TRRacun)
admin.site.register(models.Oseba)



