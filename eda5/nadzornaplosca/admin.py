from django.contrib import admin

from .models import NadzorniSistem, NadzornaEnota

class NadzornaEnotaInline(admin.TabularInline):
    model = NadzornaEnota
    extra = 0


@admin.register(NadzorniSistem)
class NadzorniSistemAdmin(admin.ModelAdmin):

    inlines = [
        NadzornaEnotaInline,
    ]


@admin.register(NadzornaEnota)
class NadzornaEnotaAdmin(admin.ModelAdmin):
    pass
