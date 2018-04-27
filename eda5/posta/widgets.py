from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget
from django.template.loader import render_to_string


class DokumentManyToManyRawIdWidget(ManyToManyRawIdWidget):

    def render(self, name, *args, **kwargs):
        popup_template = "posta/dokument/popup/popup_link.html"
        html = super(DokumentManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class DokumentForeignKeyRawIdWidget(ForeignKeyRawIdWidget):

    def render(self, name, *args, **kwargs):
        popup_template = "posta/dokument/popup/popup_link.html"
        html = super(DokumentForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus
