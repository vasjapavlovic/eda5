from django.contrib import admin

from .models import Zaznamek

@admin.register(Zaznamek)
class ZaznamekAdmin(admin.ModelAdmin):
    pass
