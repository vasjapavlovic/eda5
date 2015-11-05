from django.contrib import admin

from .models import Stevec, StevecStatus, Delilnik, Odcitek


@admin.register(Stevec)
class StevecAdmin(admin.ModelAdmin):
    pass


@admin.register(StevecStatus)
class StevecStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Delilnik)
class DelilnikAdmin(admin.ModelAdmin):
    pass


@admin.register(Odcitek)
class OdcitekAdmin(admin.ModelAdmin):
    pass
