from django.contrib import admin

from .models import Dogodek

@admin.register(Dogodek)
class DogodekAdmin(admin.ModelAdmin):

	raw_id_fields = (
		'zahtevek',
		'pomanjkljivost',
		'prijava_skode',
		'poravnava_skode',
		'prijava_policiji',
		'racun_za_popravilo')
