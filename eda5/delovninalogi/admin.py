from django.contrib import admin

from .models import Opravilo, DelovniNalog, Delo, DeloVrsta, DeloVrstaSklop, VzorecOpravila


@admin.register(Opravilo)
class OpraviloAdmin(admin.ModelAdmin):

    filter_horizontal = (
        "element",
        "pomanjkljivost",
    )
    raw_id_fields = ("element",)


@admin.register(DelovniNalog)
class DelovniNalogAdmin(admin.ModelAdmin):
    pass


@admin.register(Delo)
class DeloAdmin(admin.ModelAdmin):
    pass


@admin.register(DeloVrsta)
class DeloVrstaAdmin(admin.ModelAdmin):
    pass


@admin.register(DeloVrstaSklop)
class DeloVrstaSklopAdmin(admin.ModelAdmin):
    pass


@admin.register(VzorecOpravila)
class VzorecOpravilaAdmin(admin.ModelAdmin):
    pass
