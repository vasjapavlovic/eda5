from django.contrib import admin

# relative imports
from .models import ObrazecSplosno

# absolute imports


@admin.register(ObrazecSplosno)
class ObrazecSplosnoAdmin(admin.ModelAdmin):
	pass
