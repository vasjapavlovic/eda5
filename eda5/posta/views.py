from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import AktivnostCreateForm, DokumentCreateForm
from .models import Aktivnost, Dokument
# from .forms import PrejetaPostaCreateForm


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class PostaArhiviranjeListView(ListView):
    model = Dokument
    template_name = "posta/posta/list/extended.html"

    def get_queryset(self):
        queryset = super(PostaArhiviranjeListView, self).get_queryset()
        queryset = queryset.filter(arhiviranje=None)
        return queryset


class AktivnostCreateView(CreateView):
    model = Dokument
    #from_class = AktivnostCreateForm
    #second_form_class = DokumentCreateForm
    template_name = "posta/dokument/create.html"

    fields = (
            'oznaka',
            'naziv',
            'aktivnost',
        )

    # def get_context_data(self, *args, **kwargs):
    #     context = super(AktivnostCreateView, self).get_context_data(*args, **kwargs)
    #     context['form2'] = self.second_form_class
    #     return context
