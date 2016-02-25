from django.contrib import admin

from .models import Obvestilo, Komentar, Povezava


class KomentarInline(admin.TabularInline):
    model = Komentar
    extra = 0


@admin.register(Obvestilo)
class ObvestiloAdmin(admin.ModelAdmin):
    inlines = [
        KomentarInline,
    ]


@admin.register(Komentar)
class KomentarAdmin(admin.ModelAdmin):
    pass


@admin.register(Povezava)
class PovezavaAdmin(admin.ModelAdmin):
    pass