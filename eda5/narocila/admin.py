from django.contrib import admin

from eda5.narocila.models import Narocilo, NarociloDokument, NarociloTelefon


admin.site.register(Narocilo)
admin.site.register(NarociloDokument)
admin.site.register(NarociloTelefon)
