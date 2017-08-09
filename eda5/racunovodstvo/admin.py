from django.contrib import admin

from .models import Racun
from .models import Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska, Strosek


class StrosekInline(admin.TabularInline):
    model = Strosek
    extra = 0


class PodkontoInline(admin.TabularInline):
    model = PodKonto
    extra = 0


class SkupinaVrsteStroskaInline(admin.TabularInline):
    model = SkupinaVrsteStroska
    extra = 0


class VrstaStroskaInline(admin.TabularInline):
    model = VrstaStroska
    extra = 0


@admin.register(Racun)
class RacunAdmin(admin.ModelAdmin):

    inlines = [
        StrosekInline,
    ]

    search_fields = ['arhiviranje__dokument__oznaka']
    raw_id_fields = ("racunovodsko_leto", "povracilo_stroskov_zaposlenemu",)

@admin.register(Strosek)
class StrosekAdmin(admin.ModelAdmin):

    raw_id_fields = ("racun", "delovni_nalog", "vrsta_stroska")


@admin.register(Konto)
class KontoAdmin(admin.ModelAdmin):

    inlines = [
        PodkontoInline,
    ]


@admin.register(PodKonto)
class PodkontoAdmin(admin.ModelAdmin):

    inlines = [
        SkupinaVrsteStroskaInline,
    ]


@admin.register(SkupinaVrsteStroska)
class SkupinaVrsteStroskaAdmin(admin.ModelAdmin):

    inlines = [
        VrstaStroskaInline,
    ]


@admin.register(VrstaStroska)
class VrstaStroskaAdmin(admin.ModelAdmin):
    pass

