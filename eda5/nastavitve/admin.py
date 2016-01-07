from django.contrib import admin

from .models import NastavitevPartnerja

@admin.register(NastavitevPartnerja)
class NastavitevPartnerAdmin(admin.ModelAdmin):
    pass