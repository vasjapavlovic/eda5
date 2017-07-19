from django.shortcuts import render

from django.views.generic.edit import FormMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView


class FilteredListView(FormMixin, ListView):
    def get_form_kwargs(self):
        return {
          'initial': self.get_initial(),
          'prefix': self.get_prefix(),
          'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        form = self.get_form(self.get_form_class())

        if form.is_valid():
            self.object_list = form.filter_queryset(request, self.object_list)

        context = self.get_context_data(form=form, object_list=self.object_list)
        return self.render_to_response(context)