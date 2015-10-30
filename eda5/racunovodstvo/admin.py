from django.contrib import admin

from .models import DavcnaKlasifikacija, Racun
from .models import Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska, Strosek


admin.site.register(DavcnaKlasifikacija)
admin.site.register(Racun)
admin.site.register(Konto)
admin.site.register(PodKonto)
admin.site.register(SkupinaVrsteStroska)
admin.site.register(VrstaStroska)
admin.site.register(Strosek)
