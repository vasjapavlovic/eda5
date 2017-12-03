from django import forms

from django.template.loader import render_to_string
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget


# POPUP widgets
class DelovniNalogSelectWithPop(forms.Select):

    def render(self, name, *args, **kwargs):
        popup_template = "delovninalogi/delovninalog/popup/popup_link.html"
        html = super(DelovniNalogSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class DelovniNalogMultipleSelectWithPop(forms.SelectMultiple):

    def render(self, name, *args, **kwargs):
        popup_template = "delovninalogi/delovninalog/popup/popup_link.html"
        html = super(DelovniNalogMultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class DelovniNalogForeignKeyRawIdWidget(ForeignKeyRawIdWidget):

    def render(self, name, *args, **kwargs):
        popup_template = "delovninalogi/delovninalog/popup/popup_link.html"
        html = super(DelovniNalogForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class DelovniNalogManyToManyRawIdWidget(ManyToManyRawIdWidget):

    def render(self, name, *args, **kwargs):
        popup_template = "delovninalogi/delovninalog/popup/popup_link.html"
        html = super(DelovniNalogManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus
