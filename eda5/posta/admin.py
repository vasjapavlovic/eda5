from django.contrib import admin

from .models import Dokument, SkupinaDokumenta, Aktivnost, VrstaDokumenta, KlasifikacijaDokumenta

class VrstaDokumentaInline(admin.TabularInline):
    model = VrstaDokumenta
    extra = 0


class DokumentInline(admin.TabularInline):
    model = Dokument
    extra = 0

@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    search_fields = ['oznaka', 'naziv', 'priponka']


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


@admin.register(KlasifikacijaDokumenta)
class KlasifikacijaDokumentaAdmin(admin.ModelAdmin):

    list_display = ('oznaka', 'naziv', 'postopek_oznaka', 'postopek_naziv', 'proces_oznaka', 'proces_naziv')
    search_fields = ['oznaka', 'naziv', 'proces_oznaka', 'proces_naziv', 'postopek_oznaka', 'postopek_naziv']
