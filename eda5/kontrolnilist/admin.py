from django.contrib import admin

from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect
from .models import KontrolaVrednost

from .models import PlanAktivnost
from .models import PlanKontrolaSpecifikacija




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


@admin.register(KontrolaVrednost)
class KontrolaVrednostAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'projektno_mesto',
        'kontrola_specifikacija',
        'delovni_nalog',
        )


class PlanKontrolaSpeciikacijaInline(admin.TabularInline):
    model = PlanKontrolaSpecifikacija
    extra = 0


@admin.register(PlanAktivnost)
class PlanAktivnostAdmin(admin.ModelAdmin):

    raw_id_fields = (
        'planirano_opravilo',
        'projektno_mesto',
        )
    inlines = [
        PlanKontrolaSpeciikacijaInline,
    ]



@admin.register(PlanKontrolaSpecifikacija)
class PlanKontrolaSpecifikacijaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'plan_aktivnost',
        )
