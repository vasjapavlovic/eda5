from django.contrib import admin

from .models import Povprasevanje, Ponudba, Postavka, PonudbaPoPostavki


@admin.register(Povprasevanje)
class PovprasevanjeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ponudba)
class PonudbaAdmin(admin.ModelAdmin):
    pass


@admin.register(Postavka)
class PostavkaAdmin(admin.ModelAdmin):
    pass


@admin.register(PonudbaPoPostavki)
class PonudbaPoPostavkiAdmin(admin.ModelAdmin):
    pass