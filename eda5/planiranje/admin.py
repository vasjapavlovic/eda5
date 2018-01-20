from django.contrib import admin

from .models import SkupinaPlanov, Plan, PlaniranoOpravilo, PlaniranaAktivnost

from .models import PlanAktivnost
from .models import PlanKontrolaSkupina
from .models import PlanKontrolaSpecifikacija
from .models import PlanKontrolaSpecifikacijaOpcijaSelect
# class PlanIzdajaInline(admin.TabularInline):
#     model = PlanIzdaja
#     extra = 0


class PlaniranoOpraviloInline(admin.TabularInline):
    model = PlaniranoOpravilo
    extra = 0


class PlaniranaAktivnostInline(admin.TabularInline):
    model = PlaniranaAktivnost
    extra = 0


@admin.register(SkupinaPlanov)
class SkupinaPlanovAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = [
        PlaniranoOpraviloInline,
    ]


@admin.register(PlaniranoOpravilo)
class PlaniranoOpraviloAdmin(admin.ModelAdmin):

    pass


@admin.register(PlaniranaAktivnost)
class PlaniranaAktivnostAdmin(admin.ModelAdmin):
    pass




class PlanKontrolaSpecifikacijaInline(admin.TabularInline):
    model = PlanKontrolaSpecifikacija
    extra = 0
    raw_id_fields = (
        'plan_kontrola_skupina',
        'projektno_mesto',
        )

class PlanKontrolaSkupinaInline(admin.TabularInline):
    model = PlanKontrolaSkupina
    extra = 0

@admin.register(PlanAktivnost)
class PlanAktivnostAdmin(admin.ModelAdmin):

    raw_id_fields = (
        'planirano_opravilo',
        )
    inlines = [
        PlanKontrolaSkupinaInline,
    ]


class PlanKontrolaSpecifikacijaOpcijaSelectInline(admin.TabularInline):
    model = PlanKontrolaSpecifikacijaOpcijaSelect
    extra = 0


@admin.register(PlanKontrolaSkupina)
class PlanKontrolaSkupinaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'plan_aktivnost',
        )

    inlines = [
        PlanKontrolaSpecifikacijaInline,
    ]



@admin.register(PlanKontrolaSpecifikacija)
class PlanKontrolaSpecifikacijaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'plan_kontrola_skupina',
        'projektno_mesto',
        )

    inlines = [
        PlanKontrolaSpecifikacijaOpcijaSelectInline,
    ]


@admin.register(PlanKontrolaSpecifikacijaOpcijaSelect)
class PlanKontrolaSpecifikacijaAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'plan_kontrola_specifikacija',
        )
