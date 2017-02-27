from django.contrib import admin

from .models import Stavba, Etaza, Prostor


# ---------------------------------------
# Inlines
# ---------------------------------------

# ETAŽA
class EtazaInLine(admin.TabularInline):
    model = Etaza
    extra = 0

# PROSTOR
class ProstorInLine(admin.TabularInline):
    model = Prostor
    extra = 0


# ---------------------------------------
# Models
# ---------------------------------------

# STAVBA
@admin.register(Stavba)
class StavbaAdmin(admin.ModelAdmin):
    list_display = ("oznaka", "naziv")
    search_fields = ["oznaka", "naziv", ]
    ordering = ["oznaka"]
    # readonly_fields = ["stevilka",]
    inlines = [
        EtazaInLine,
    ]

# ETAŽA
@admin.register(Etaza)
class EtazaAdmin(admin.ModelAdmin):
    list_display = ("oznaka", "naziv")
    search_fields = ["oznaka", "naziv", ]
    ordering = ["oznaka"]
    # readonly_fields = ["stevilka",]
    inlines = [
        ProstorInLine,
    ]

# PROSTOR
@admin.register(Prostor)
class ProstorAdmin(admin.ModelAdmin):
    list_display = ("oznaka", "naziv")
    search_fields = ["oznaka", "naziv", ]
    ordering = ["oznaka"]
    # readonly_fields = ["stevilka",]


