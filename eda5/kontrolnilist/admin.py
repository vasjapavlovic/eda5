from django.contrib import admin

from .models import Aktivnost
from .models import AktivnostParameterSpecifikacija
from .models import OpcijaSelect




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
