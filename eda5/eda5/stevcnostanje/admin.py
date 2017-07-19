from django.contrib import admin

from .models import Stevec, StevecStatus, Delilnik, Odcitek


@admin.register(Stevec)
class StevecAdmin(admin.ModelAdmin):
    search_fields = ['naziv']


@admin.register(StevecStatus)
class StevecStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Delilnik)
class DelilnikAdmin(admin.ModelAdmin):
    search_fields = ['oznaka']


@admin.register(Odcitek)
class OdcitekAdmin(admin.ModelAdmin):
    pass
