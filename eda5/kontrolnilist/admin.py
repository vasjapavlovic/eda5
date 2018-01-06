from django.contrib import admin

from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect




@admin.register(Aktivnost)
class AktivnostAdmin(admin.ModelAdmin):

    raw_id_fields = (
        'projektno_mesto',
        'opravilo',
        )

@admin.register(KontrolaSpecifikacija)
class KontrolaSpecifikacijaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'aktivnost',
        )


@admin.register(KontrolaSpecifikacijaOpcijaSelect)
class KontrolaSpecifikacijaOpcijaSelectAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'kontrola_specifikacija',
        )
