from django.contrib import admin


from .models import SkupinaDokumenta, VrstaDokumenta, Dokument

admin.site.register(SkupinaDokumenta)
admin.site.register(VrstaDokumenta)


@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    pass
