from django.contrib import admin

from . import models


@admin.register(models.Pomanjkljivost)
class PomanjkljivostAdmin(admin.ModelAdmin):
    
    raw_id_fields = ("element",)


@admin.register(models.Naloga)
class NalogaAdmin(admin.ModelAdmin):
    pass