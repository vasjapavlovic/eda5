from django.contrib import admin

from eda5.sestanki.models import Sestanek, Tema, Tocka, Sklep, OpombaSklepa


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


@admin.register(OpombaSklepa)
class OpombaSklepaAdmin(admin.ModelAdmin):
    raw_id_fields = ("sklep",)