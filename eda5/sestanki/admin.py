from django.contrib import admin

from eda5.sestanki.models import Sestanek, TemaSestankov, TockaSestanka, AlinejaSestanka


@admin.register(Sestanek)
class SestanekAdmin(admin.ModelAdmin):
    filter_horizontal = ('udelezenci', )


@admin.register(TemaSestankov)
class TemaSestankovAdmin(admin.ModelAdmin):
    pass


@admin.register(TockaSestanka)
class TockaSestankaAdmin(admin.ModelAdmin):
    pass


@admin.register(AlinejaSestanka)
class AlinejaSestankaAdmin(admin.ModelAdmin):
   filter_horizontal = ('predlagal', 'proti_predlogu')