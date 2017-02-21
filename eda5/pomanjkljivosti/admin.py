from django.contrib import admin

from . import models


@admin.register(models.Pomanjkljivost)
class PomanjkljivostAdmin(admin.ModelAdmin):
    
    filter_horizontal = ['element', ]
