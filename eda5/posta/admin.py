from django.contrib import admin

from .models import Dokument, SkupinaDokumenta, Aktivnost, VrstaDokumenta


@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Aktivnost)
class PostnaStoritevAdmin(admin.ModelAdmin):
    pass


@admin.register(SkupinaDokumenta)
class SkupinaDokumentaAdmin(admin.ModelAdmin):
    pass


@admin.register(VrstaDokumenta)
class VrstaDokumentaAdmin(admin.ModelAdmin):
    pass
