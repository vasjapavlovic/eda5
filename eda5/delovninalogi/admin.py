from django.contrib import admin

from .models import Opravilo, DelovniNalog, Delo


@admin.register(Opravilo)
class OpraviloAdmin(admin.ModelAdmin):
    filter_horizontal = ("element",)


@admin.register(DelovniNalog)
class DelovniNalogAdmin(admin.ModelAdmin):
    filter_horizontal = ("dokument",)


@admin.register(Delo)
class DeloAdmin(admin.ModelAdmin):
    pass
