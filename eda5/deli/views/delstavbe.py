# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render
from django.utils import timezone

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Stavba, Skupina, Podskupina, DelStavbe, ProjektnoMesto, Element
from eda5.delovninalogi.models import Opravilo, DelovniNalog
from eda5.katalog.models import ObratovalniParameter
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek

# Forms
from ..forms import skupina_forms, podskupina_forms, delstavbe_forms
from ..forms import projektnomesto_forms, element_forms, nastavitev_forms

# templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse
from eda5.reports.forms.forms import FormatForm



class DelCreateView(LoginRequiredMixin, CreateView):

    model = DelStavbe
    form_class = delstavbe_forms.DelCreateForm
    template_name = "deli/delstavbe/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelCreateView, self).get_context_data(*args, **kwargs)
        context['skupina_izbira_form'] = skupina_forms.SkupinaIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class DelUpdateView(LoginRequiredMixin, UpdateView):

    model = DelStavbe
    form_class = delstavbe_forms.DelUpdateForm
    template_name = "deli/delstavbe/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelUpdateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context



class DelListView(LoginRequiredMixin, ListView):
    template_name = "deli/delstavbe/list/base.html"
    model = DelStavbe  # prej je bila tu Skupina

    def get_context_data(self, *args, **kwargs):
        context = super(DelListView, self).get_context_data(*args, **kwargs)
        context['del_form'] = delstavbe_forms.DelCreateForm

        seznam_delov_AA = DelStavbe.objects.filter(podskupina__oznaka="AA")
        context['seznam_delov_AA'] = seznam_delov_AA

        modul_zavihek = Zavihek.objects.get(oznaka="DEL_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_queryset(self, **kwargs):
        queryset = DelStavbe.objects.all().order_by(
            "podskupina__skupina",
            "podskupina",
            "oznaka",
            )
        return queryset

    def post(self, request, *args, **kwargs):
        del_form = delstavbe_forms.DelCreateForm(request.POST or None)

        # avtomatska oznaka Dela stavbe

        if del_form.is_valid():

            # vnešeni podatki
            podskupina = del_form.cleaned_data['podskupina']
            naziv = del_form.cleaned_data['naziv']
            shema = del_form.cleaned_data['shema']
            lastniska_skupina = del_form.cleaned_data['lastniska_skupina']

            # avtomatska oznaka
            st_delov = DelStavbe.objects.filter(podskupina=podskupina).count()
            if st_delov > 9:
                oznaka = str(podskupina.oznaka) + str(st_delov + 1)
            else:
                oznaka = str(podskupina.oznaka) + '0' + str(st_delov + 1)

            DelStavbe.objects.create_del(
                                         podskupina=podskupina,
                                         oznaka=oznaka,
                                         naziv=naziv,
                                         shema=shema,
                                         lastniska_skupina=lastniska_skupina,
                                         )

        return HttpResponseRedirect(reverse('moduli:deli:del_list'))


class DelDetailView(LoginRequiredMixin, DetailView):
    template_name = "deli/delstavbe/detail/base.html"
    model = DelStavbe

    def get_context_data(self, *args, **kwargs):
        context = super(DelDetailView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="DEL_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # Servisna knjiga
        delstavbe_instance = DelStavbe.objects.get(id=self.object.id)

        # seznam delovnih nalogov (za servisno knjigo)
        servisna_knjiga = []
        # seznam opravil kjer je vsebovan element
        opravila = Opravilo.objects.filter(element__del_stavbe=self.object.id)
        # iteriramo skozi seznam opravil, da pridobimo posamezne sezname delovnih nalogov
        for opravilo in opravila:
            delovninalog_list_x = DelovniNalog.objects.filter(opravilo=opravilo)
        # iteriramo skozi seznam delovnih nalogov in dodamo v seznam
            for dn in delovninalog_list_x:
                servisna_knjiga.append(dn)
            # list(delovninalog_list)
        context['servisna_knjiga'] = servisna_knjiga


        return context


class DelStavbePrintView(LoginRequiredMixin, UpdateView):
    model = Stavba
    template_name = 'deli/delstavbe/delstavbe_print.html'
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(DelStavbePrintView, self).get_context_data(*args, **kwargs)

        form = FormatForm()
        context['form'] = form

        stavba = Stavba.objects.get(id=1)
        del_stavbe_list = DelStavbe.objects.filter(stavba=stavba)
        del_stavbe_list = del_stavbe_list.filter(is_active=True)
        del_stavbe_list = del_stavbe_list.order_by(
            'podskupina__skupina',
            'podskupina',
            'oznaka',
        )

        print_data = {
            'stavba': stavba,
            'del_stavbe_list': del_stavbe_list,

        }

        context['print_data'] = print_data
        return context


    def post(self, request, *args, **kwargs):

        stavba = Stavba.objects.get(id=1)
        del_stavbe_list = DelStavbe.objects.filter(stavba=stavba)
        del_stavbe_list = del_stavbe_list.filter(is_active=True)
        del_stavbe_list = del_stavbe_list.order_by(
            'podskupina__skupina',
            'podskupina',
            'oznaka',
        )

        print_data = {
            'stavba': stavba,
            'del_stavbe_list': del_stavbe_list,

        }


        form = FormatForm(request.POST or None)
        # deli_seznam_filter_form = DeliSeznamFilterForm(request.POST or None)

        form_is_valid = False
        # deli_seznam_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        # if deli_seznam_filter_form.is_valid():
        #     program = deli_seznam_filter_form.cleaned_data['program']
        #     deli_filter_list = DelStavbe.objects.filter(lastniska_skupina__program=program)
        #     deli_seznam_filter_form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()


            # prenos podatkov za aplikacijo templated_docs

            filename = fill_template(
                'obrazci/delstavbe/seznam_delov_stavbe.ods', {'print_data': print_data, 'datum_danes': datum_danes}, output_format=doctypex)
            visible_filename = 'Seznam delov stavbe {}.{}'.format(stavba.naziv, doctypex)

            return FileResponse(filename, visible_filename)


        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                # 'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )
