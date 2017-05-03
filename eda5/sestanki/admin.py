from django.contrib import admin

from eda5.sestanki.models import Sestanek, Tema, Zadeva, Tocka, Vnos, OpombaVnosa



class TockaInlines(admin.TabularInline):
    model = Tocka
    extra = 0



@admin.register(Sestanek)
class SestanekAdmin(admin.ModelAdmin):
    raw_id_fields = ("sklicatelj", "prisotni", )
    inlines = [
        TockaInlines,
    ]


@admin.register(Tema)
class ZadevaAdmin(admin.ModelAdmin):
    pass

@admin.register(Zadeva)
class ZadevaAdmin(admin.ModelAdmin):
    pass


@admin.register(Tocka)
class TockaAdmin(admin.ModelAdmin):
    pass


@admin.register(Vnos)
class SklepAdmin(admin.ModelAdmin):
    raw_id_fields = ("dopolnitev_vnosov",)


@admin.register(OpombaVnosa)
class OpombaVnosaAdmin(admin.ModelAdmin):
    raw_id_fields = ("vnos",)