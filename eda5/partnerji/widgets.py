from django import forms

from django.template.loader import render_to_string
from django.contrib.admin.widgets import ForeignKeyRawIdWidget, ManyToManyRawIdWidget


# POPUP widgets
class PartnerSelectWithPop(forms.Select):

    def render(self, name, *args, **kwargs):
        popup_template = "partnerji/partner/popup/popup_link.html"
        html = super(PartnerSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class PartnerMultipleSelectWithPop(forms.SelectMultiple):
    
    def render(self, name, *args, **kwargs):
        popup_template = "partnerji/partner/popup/popup_link.html"
        html = super(PartnerMultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class PartnerForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "partnerji/partner/popup/popup_link.html"
        html = super(PartnerForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

class PartnerManyToManyRawIdWidget(ManyToManyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "partnerji/partner/popup/popup_link.html"
        html = super(PartnerManyToManyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus


class OsebaForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    
    def render(self, name, *args, **kwargs):
        popup_template = "partnerji/oseba/popup/popup_link.html"
        html = super(OsebaForeignKeyRawIdWidget, self).render(name, *args, **kwargs)
        popupplus = render_to_string(popup_template, {'field': name})
        return html+popupplus

