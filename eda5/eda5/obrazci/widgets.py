from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget
from django.template.loader import render_to_string


class DopisManyToManyRawIdWidget(ManyToManyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "obrazci/dopis/popup/popup_link.html"
        html = super(DopisManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus