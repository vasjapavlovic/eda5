from django.contrib import admin


from .models import SkupinaDokumenta, VrstaDokumenta, Dokument

admin.site.register(SkupinaDokumenta)
admin.site.register(VrstaDokumenta)
admin.site.register(Dokument)
