from django.contrib import admin

from .models import Modul, Zavihek


class ZavihekInline(admin.TabularInline):
    model = Zavihek
    extra = 0


@admin.register(Modul)
class ModulAdmin(admin.ModelAdmin):

    inlines = [
        ZavihekInline,
    ]


@admin.register(Zavihek)
class ZavihekAdmin(admin.ModelAdmin):
    filter_horizontal = ('parent', )
