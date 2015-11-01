from django.contrib import admin

from .models import SklopPlanov, Plan, PlanIzdaja, PlanOpravilo


@admin.register(SklopPlanov)
class SklopPlanovAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanIzdaja)
class PlanIzdajaAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanOpravilo)
class PlanOpraviloAdmin(admin.ModelAdmin):
    pass
