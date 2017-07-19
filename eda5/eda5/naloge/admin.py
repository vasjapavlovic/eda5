from django.contrib import admin

from . import models


@admin.register(models.Naloga)
class NalogaAdmin(admin.ModelAdmin):
    
    pass