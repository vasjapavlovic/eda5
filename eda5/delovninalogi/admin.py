from django.contrib import admin

from .models import Opravilo, DelovniNalog, Delo, DeloVrsta, DeloVrstaSklop, VzorecOpravila
from .models import Aktivnost
from .models import AktivnostParameterSpecifikacija
from .models import OpcijaSelect


@admin.register(Opravilo)
class OpraviloAdmin(admin.ModelAdmin):

    filter_horizontal = (

        "pomanjkljivost",
    )
    raw_id_fields = (
        "zahtevek",
        "narocilo",
        "element",
        "vrsta_stroska",
        "nosilec",
        'planirano_opravilo',
        "pomanjkljivost",
        'naloga',
        )


@admin.register(DelovniNalog)
class DelovniNalogAdmin(admin.ModelAdmin):
    search_fields = ['oznaka', 'opravilo__naziv']


@admin.register(Delo)
class DeloAdmin(admin.ModelAdmin):
    pass


@admin.register(DeloVrsta)
class DeloVrstaAdmin(admin.ModelAdmin):
    pass


@admin.register(DeloVrstaSklop)
class DeloVrstaSklopAdmin(admin.ModelAdmin):
    pass


@admin.register(VzorecOpravila)
class VzorecOpravilaAdmin(admin.ModelAdmin):

    raw_id_fields = (
        "narocilo",
        "element",
        "vrsta_stroska",
        "nosilec",
        'planirano_opravilo',
        )



@admin.register(Aktivnost)
class AktivnostAdmin(admin.ModelAdmin):

    raw_id_fields = (
        'projektno_mesto',
        'opravilo',
        )

@admin.register(AktivnostParameterSpecifikacija)
class AktivnostParamaterSpecifikacijaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'aktivnost',
        )


@admin.register(OpcijaSelect)
class OpcijaSelectAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'aktivnost_parameter_specifikacija',
        )
