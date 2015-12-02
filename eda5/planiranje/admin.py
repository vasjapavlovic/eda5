from django.contrib import admin

from .models import SkupinaPlanov, Plan, PlaniranoOpravilo, PlaniranaAktivnost

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



# @admin.register(PlanIzdaja)
# class PlanIzdajaAdmin(admin.ModelAdmin):
#     # inlines = [
#     #     PlanOpraviloInline,
#     # ]
#     pass


@admin.register(PlaniranoOpravilo)
class PlaniranoOpraviloAdmin(admin.ModelAdmin):
    pass


@admin.register(PlaniranaAktivnost)
class PlaniranaAktivnostAdmin(admin.ModelAdmin):
    pass
