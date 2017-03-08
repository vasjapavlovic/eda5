from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget
from django.template.loader import render_to_string


class ArhiviranjeManyToManyRawIdWidget(ManyToManyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "arhiv/arhiviranje/popup/popup_link.html"
        html = super(ArhiviranjeManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus