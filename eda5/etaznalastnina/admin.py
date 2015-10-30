from django.contrib import admin

from .models import LastniskaEnotaElaborat, LastniskaEnotaInterna
from .models import Program, LastniskaSkupina


class LastniskaSkupinaAdmin(admin.ModelAdmin):
    filter_horizontal = ('lastniska_enota',)

    class Meta:
        model = LastniskaSkupina


admin.site.register(LastniskaEnotaElaborat)
admin.site.register(LastniskaEnotaInterna)
admin.site.register(Program)
admin.site.register(LastniskaSkupina, LastniskaSkupinaAdmin)
