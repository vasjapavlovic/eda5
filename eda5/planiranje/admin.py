from django.contrib import admin

from .models import SklopPlanov, Plan, PlanIzdaja, PlanOpravilo

class PlanIzdajaInline(admin.TabularInline):
    model = PlanIzdaja
    extra = 0


class PlanOpraviloInline(admin.TabularInline):
    model = PlanOpravilo
    extra = 0


@admin.register(SklopPlanov)
class SklopPlanovAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = [
        PlanIzdajaInline,
    ]


@admin.register(PlanIzdaja)
class PlanIzdajaAdmin(admin.ModelAdmin):
    inlines = [
        PlanOpraviloInline,
    ]


@admin.register(PlanOpravilo)
class PlanOpraviloAdmin(admin.ModelAdmin):
    pass
