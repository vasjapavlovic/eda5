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



# class ForeignKeyRawIdWidget(forms.TextInput):
#     """
#     A Widget for displaying ForeignKeys in the "raw_id" interface rather than
#     in a <select> box.
#     """
#     template_name = 'admin/widgets/foreign_key_raw_id.html'

#     def __init__(self, rel, admin_site, attrs=None, using=None):
#         self.rel = rel
#         self.admin_site = admin_site
#         self.db = using
#         super().__init__(attrs)

#     def get_context(self, name, value, attrs=None):
#         context = super().get_context(name, value, attrs)
#         rel_to = self.rel.model
#         if rel_to in self.admin_site._registry:
#             # The related object is registered with the same AdminSite
#             related_url = reverse(
#                 'admin:%s_%s_changelist' % (
#                     rel_to._meta.app_label,
#                     rel_to._meta.model_name,
#                 ),
#                 current_app=self.admin_site.name,
#             )

#             params = self.url_parameters()
#             if params:
#                 related_url += '?' + '&amp;'.join(
#                     '%s=%s' % (k, v) for k, v in params.items(),
#                 )
#             context['related_url'] = mark_safe(related_url)
#             context['link_title'] = _('Lookup')
#             # The JavaScript code looks for this class.
#             context['widget']['attrs'].setdefault('class', 'vForeignKeyRawIdAdminField')
#         if context['widget']['value']:
#             context['link_label'], context['link_url'] = self.label_and_url_for_value(value)
#         return context

#     def base_url_parameters(self):
#         limit_choices_to = self.rel.limit_choices_to
#         if callable(limit_choices_to):
#             limit_choices_to = limit_choices_to()
#         return url_params_from_lookup_dict(limit_choices_to)

#     def url_parameters(self):
#         from django.contrib.admin.views.main import TO_FIELD_VAR
#         params = self.base_url_parameters()
#         params.update({TO_FIELD_VAR: self.rel.get_related_field().name})
#         return params

#     def label_and_url_for_value(self, value):
#         key = self.rel.get_related_field().name
#         try:
#             obj = self.rel.model._default_manager.using(self.db).get(**{key: value})
#         except (ValueError, self.rel.model.DoesNotExist):
#             return '', ''

#         try:
#             url = reverse(
#                 '%s:%s_%s_change' % (
#                     self.admin_site.name,
#                     obj._meta.app_label,
#                     obj._meta.object_name.lower(),
#                 ),
#                 args=(obj.pk,)
#             )
#         except NoReverseMatch:
#             url = ''  # Admin not registered for target model.

#         return Truncator(obj).words(14, truncate='...'), url



# class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
#     """
#     A Widget for displaying ManyToMany ids in the "raw_id" interface rather than
#     in a <select multiple> box.
#     """
#     template_name = "core/popupplus.html"

#     def get_context(self, name, value, attrs=None):
#         context = super().get_context(name, value, attrs)
#         if self.rel.model in self.admin_site._registry:
#             # The related object is registered with the same AdminSite
#             context['widget']['attrs']['class'] = 'vManyToManyRawIdAdminField'
#         return context

#     def url_parameters(self):
#         return self.base_url_parameters()

#     def label_and_url_for_value(self, value):
#         return '', ''

#     def value_from_datadict(self, data, files, name):
#         value = data.get(name)
#         if value:
#             return value.split(',')

#     def format_value(self, value):
#         return ','.join(force_text(v) for v in value) if value else ''