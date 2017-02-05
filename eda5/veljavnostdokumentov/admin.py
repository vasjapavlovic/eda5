from django.contrib import admin

from .models import VeljavnostDokumenta


@admin.register(VeljavnostDokumenta)
class VeljavnostDokumentaAdmin(admin.ModelAdmin):
    pass
