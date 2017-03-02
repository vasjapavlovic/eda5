from django import forms

from django.template.loader import render_to_string
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget




# POPUP widgets
class ProjektnoMestoSelectWithPop(forms.Select):

    def render(self, name, *args, **kwargs):
        popup_template = "deli/projektnomesto/popup/popup_link.html"
        html = super(ProjektnoMestoSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class ProjektnoMestoMultipleSelectWithPop(forms.SelectMultiple):
    
    def render(self, name, *args, **kwargs):
        popup_template = "deli/projektnomesto/popup/popup_link.html"
        html = super(ProjektnoMestoMultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class ProjektnoMestoForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "deli/projektnomesto/popup/popup_link.html"
        html = super(ProjektnoMestoForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class ProjektnoMestoManyToManyRawIdWidget(ManyToManyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "deli/projektnomesto/popup/popup_link.html"
        html = super(ProjektnoMestoManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

