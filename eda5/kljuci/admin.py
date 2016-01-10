from django.contrib import admin

from .models import SklopKljucev, Kljuc, PredajaKljucev


@admin.register(SklopKljucev)
class SklopKljucevAdmin(admin.ModelAdmin):
    pass


@admin.register(Kljuc)
class KljucAdmin(admin.ModelAdmin):
    pass


@admin.register(PredajaKljucev)
class PredajaKljucevAdmin(admin.ModelAdmin):
    pass
