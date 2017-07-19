from django.contrib import admin

from .models import PredajaLastnine, ProdajaLastnine, NajemLastnine


class ProdajaLastnineInline(admin.TabularInline):
    model = ProdajaLastnine
    extra = 0


class NajemLastnineInline(admin.TabularInline):
    model = NajemLastnine
    extra = 0


@admin.register(PredajaLastnine)
class PredajaLastnineAdmin(admin.ModelAdmin):
    inlines = [
        ProdajaLastnineInline,
        NajemLastnineInline,
        ]


@admin.register(ProdajaLastnine)
class ProdajaLastnineAdmin(admin.ModelAdmin):
    pass


@admin.register(NajemLastnine)
class NajemLastnineAdmin(admin.ModelAdmin):
    pass
