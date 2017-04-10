from django.contrib import admin

from eda5.sestanki.models import Sestanek, Tema, Tocka, Sklep


@admin.register(Sestanek)
class SestanekAdmin(admin.ModelAdmin):
    raw_id_fields = ("sklicatelj", "prisotni", )


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Tocka)
class TockaAdmin(admin.ModelAdmin):
    pass


@admin.register(Sklep)
class SklepAdmin(admin.ModelAdmin):
    raw_id_fields = ("dopolnitev_sklepov",)