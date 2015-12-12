from django.contrib import admin

from .models import Dokument, SkupinaDokumenta, Aktivnost, VrstaDokumenta

class VrstaDokumentaInline(admin.TabularInline):
    model = VrstaDokumenta
    extra = 0


class DokumentInline(admin.TabularInline):
    model = Dokument
    extra = 0

@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Aktivnost)
class PostnaStoritevAdmin(admin.ModelAdmin):
    pass


@admin.register(SkupinaDokumenta)
class SkupinaDokumentaAdmin(admin.ModelAdmin):
    inlines = [
        VrstaDokumentaInline,
    ]


@admin.register(VrstaDokumenta)
class VrstaDokumentaAdmin(admin.ModelAdmin):
    inlines = [
        DokumentInline,
    ]
