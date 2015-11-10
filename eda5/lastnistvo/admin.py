from django.contrib import admin

from .models import Najem, Prodaja

@admin.register(Najem)
class NajemAdmin(admin.ModelAdmin):
    filter_horizontal = ['lastniska_enota']


@admin.register(Prodaja)
class ProdajaAdmin(admin.ModelAdmin):
    filter_horizontal = ['lastniska_enota']


