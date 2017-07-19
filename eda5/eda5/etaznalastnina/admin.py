from django.contrib import admin

from .models import LastniskaEnotaElaborat, LastniskaEnotaInterna
from .models import Program, LastniskaSkupina, InternaDodatno, UporabnoDovoljenje


class LastniskaEnotaInternaInline(admin.TabularInline):
    model = LastniskaEnotaInterna
    extra = 0


class InternaDodatnoInline(admin.TabularInline):
    model = InternaDodatno
    extra = 0


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(LastniskaEnotaElaborat)
class LastniskaEnotaElaboratAdmin(admin.ModelAdmin):

    search_fields = ('oznaka',)

    inlines = [
        LastniskaEnotaInternaInline,
    ]


@admin.register(LastniskaEnotaInterna)
class LastniskaEnotaInternaAdmin(admin.ModelAdmin):

    search_fields = ('oznaka',)

    inlines = [
        InternaDodatnoInline,
    ]


@admin.register(LastniskaSkupina)
class LastniskaSkupinaAdmin(admin.ModelAdmin):

    filter_horizontal = ('lastniska_enota',)


@admin.register(InternaDodatno)
class InternaDodatnoAdmin(admin.ModelAdmin):
    pass


@admin.register(UporabnoDovoljenje)
class UporabnoDovoljenjeAdmin(admin.ModelAdmin):
    list_display = ('st_dokumenta', 'oznaka', 'datum', 'objekt')
