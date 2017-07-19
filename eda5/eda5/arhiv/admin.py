from django.contrib import admin


from .models import Arhiv, ArhivMesto, Arhiviranje


@admin.register(Arhiv)
class ArhivAdmin(admin.ModelAdmin):
    pass


@admin.register(ArhivMesto)
class ArhivMestoAdmin(admin.ModelAdmin):
    pass


@admin.register(Arhiviranje)
class ArhiviranjeAdmin(admin.ModelAdmin):
    search_fields = ['dokument__oznaka', 'dokument__naziv', 'dokument__priponka']
