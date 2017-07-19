from django.contrib import admin

from .models import Dogodek

@admin.register(Dogodek)
class DogodekAdmin(admin.ModelAdmin):
	pass