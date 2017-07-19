from django.contrib import admin

from .models import Reklamacija

@admin.register(Reklamacija)
class ReklamacijaAdmin(admin.ModelAdmin):
	pass
