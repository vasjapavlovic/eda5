from django.contrib import admin

from .models import PredpisSklop, PredpisPodsklop, PredpisOpravilo, Predpis


class PredpisPodsklopInline(admin.TabularInline):
    model = PredpisPodsklop
    extra = 0


class PredpisOpraviloInline(admin.TabularInline):
    model = PredpisOpravilo
    extra = 0


@admin.register(PredpisSklop)
class PredpisSklopAdmin(admin.ModelAdmin):

    inlines = [
        PredpisPodsklopInline,
    ]


@admin.register(PredpisPodsklop)
class PredpisPodsklopAdmin(admin.ModelAdmin):

    inlines = [
        PredpisOpraviloInline,
    ]



@admin.register(PredpisOpravilo)
class PredpisOpraviloAdmin(admin.ModelAdmin):

    filter_horizontal = ('predpis',)


@admin.register(Predpis)
class PredpisAdmin(admin.ModelAdmin):
    pass



