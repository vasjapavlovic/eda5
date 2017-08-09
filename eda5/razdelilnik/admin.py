from django.contrib import admin

from .models import Razdelilnik, StrosekLE, StrosekRazdelilnik, StrosekDelitevVrsta, StrosekKljucDelitve
from .models import StrosekRazdelilnikPostavka

admin.site.register(StrosekRazdelilnikPostavka)
admin.site.register(StrosekDelitevVrsta)
admin.site.register(StrosekKljucDelitve)
admin.site.register(StrosekLE)


class StrosekRazdelilnikInline(admin.TabularInline):
    model = StrosekRazdelilnik
    extra = 0

    # stroškov je veliko. Zato jih ne prikažemo z dropdown
    raw_id_fields = ("strosek",)

    
@admin.register(Razdelilnik)
class RazdelilnikAdmin(admin.ModelAdmin):
    inlines = [
        StrosekRazdelilnikInline,
    ]


class StrosekRazdelilnikPostavkaInline(admin.TabularInline):
    model = StrosekRazdelilnikPostavka
    extra = 0


@admin.register(StrosekRazdelilnik)
class StrosekRazdelilnikAdmin(admin.ModelAdmin):
    raw_id_fields = ("strosek",)
    inlines = [
        StrosekRazdelilnikPostavkaInline,
    ]