from django.contrib import admin

from .models import SklopKljucev, Kljuc, PredajaKljuca


@admin.register(SklopKljucev)
class SklopKljucevAdmin(admin.ModelAdmin):
    pass


@admin.register(Kljuc)
class KljucAdmin(admin.ModelAdmin):
    pass


@admin.register(PredajaKljuca)
class PredajaKljucaAdmin(admin.ModelAdmin):
    pass
