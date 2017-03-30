from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget
from django.template.loader import render_to_string


class ZahtevekForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "zahtevki/zahtevek/popup/popup_link.html"
        html = super(ZahtevekForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus


class ZahtevekManyToManyRawIdWidget(ManyToManyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "zahtevki/zahtevek/popup/popup_link.html"
        html = super(ZahtevekManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus