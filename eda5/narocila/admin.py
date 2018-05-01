from django.contrib import admin

from eda5.narocila.models import Narocilo, NarociloDokument, NarociloTelefon




class NarociloDokumentInline(admin.TabularInline):
    model = NarociloDokument
    extra = 0
    raw_id_fields = (
        'dokument',
        )


class NarociloTelefonInline(admin.TabularInline):
    model = NarociloTelefon
    extra = 0


@admin.register(Narocilo)
class NarociloAdmin(admin.ModelAdmin):
    search_fields = ('oznaka', 'predmet')
    inlines = [
        NarociloDokumentInline,
        #NarociloTelefonInline,
    ]



@admin.register(NarociloDokument)
class NarociloAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'dokument',
        )


@admin.register(NarociloTelefon)
class NarociloAdmin(admin.ModelAdmin):
    pass
