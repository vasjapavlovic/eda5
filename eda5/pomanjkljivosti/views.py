from django.views import generic
from . import models, forms


class PomanjkljivostiHomeView(generic.TemplateView):
    template_name = "pomanjkljivosti/home.html"


class PomanjkljivostCreateView(generic.CreateView):
    model = models.Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/form.html"
    form_class = forms.PomanjkljivostCreateForm


class PomanjkljivostListView(generic.ListView):
    model = models.Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/list.html"

    def get_queryset(self):
        queryset = super(PomanjkljivostListView, self).get_queryset()
        queryset = self.model.objects.filter(is_likvidiran=False)
        return queryset


class PomanjkljivostDetailView(generic.DetailView):
    model = models.Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/detail/base.html"