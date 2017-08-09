# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Razdelilnik, StrosekRazdelilnik
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms.razdelilnik_forms import RazdelilnikSearchForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView



class RazdelilnikListView(LoginRequiredMixin, FilteredListView):
    model = Razdelilnik
    form_class= RazdelilnikSearchForm
    template_name = "razdelilnik/razdelilnik/list/base.html"
    paginate_by = 30

    def get_context_data(self, *args, **kwargs):
        context = super(RazdelilnikListView, self).get_context_data(*args, **kwargs)

        # content
        # context['zahtevki_vresevanju_list'] = self.model.objects.zahtevki_vresevanju()
        # context['zahtevki_zakljuceni_list'] = self.model.objects.zahtevki_zakljuceni()

        modul_zavihek = Zavihek.objects.get(oznaka="RAZDELILNIK_LIST")
        context['modul_zavihek'] = modul_zavihek
        return context


###########################################################
# Reklamacija Detail View
#----------------------------------------------------------
class RazdelilnikDetailView(LoginRequiredMixin, DetailView):
    model = Razdelilnik
    template_name = "razdelilnik/razdelilnik/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RazdelilnikDetailView, self).get_context_data(*args, **kwargs)

        strosekrazdelilnik_list = StrosekRazdelilnik.objects.filter(razdelilnik=self.object)
        context['strosekrazdelilnik_list'] = strosekrazdelilnik_list

        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        context['zaznamek_list'] = Zaznamek.objects.filter(razdelilnik=self.object.id).order_by('-datum', '-ura')

        context['strosekrazdelilnik_list'] = StrosekRazdelilnik.objects.filter(
            razdelilnik=self.object.id).annotate(vrednost_osnova=Sum('strosek__osnova'))

        vrednost_razdelilnik_osnova = StrosekRazdelilnik.objects.filter(
            razdelilnik=self.object.id).aggregate(vrednost=Sum('strosek__osnova'))

        context['vrednost_razdelilnik_osnova'] = vrednost_razdelilnik_osnova

        vrednost_razdelilnik_ddvbrez = StrosekRazdelilnik.objects.filter(
            razdelilnik=self.object.id, strosek__stopnja_ddv=0).aggregate(vrednost=Sum('strosek__osnova')*1)

        vrednost_razdelilnik_ddvnizja = StrosekRazdelilnik.objects.filter(
            razdelilnik=self.object.id, strosek__stopnja_ddv=1).aggregate(vrednost=Sum('strosek__osnova')*1.095)

        vrednost_razdelilnik_ddvvisja = StrosekRazdelilnik.objects.filter(
            razdelilnik=self.object.id, strosek__stopnja_ddv=2).aggregate(vrednost=Sum('strosek__osnova')*1.22)

        if vrednost_razdelilnik_ddvbrez['vrednost'] == None:
            vrednost_razdelilnik_ddvbrez['vrednost'] = 0

        if vrednost_razdelilnik_ddvnizja['vrednost'] == None:
            vrednost_razdelilnik_ddvnizja['vrednost'] = 0

        if vrednost_razdelilnik_ddvvisja['vrednost'] == None:
            vrednost_razdelilnik_ddvvisja['vrednost'] = 0


        context['vrednost_razdelilnik_ddvbrez'] = vrednost_razdelilnik_ddvbrez
        context['vrednost_razdelilnik_ddvnizja'] = vrednost_razdelilnik_ddvnizja
        context['vrednost_razdelilnik_ddvvisja'] = vrednost_razdelilnik_ddvvisja

        context['vrednost_razdelilnik_zddv'] = vrednost_razdelilnik_ddvbrez['vrednost'] + vrednost_razdelilnik_ddvnizja['vrednost'] + vrednost_razdelilnik_ddvvisja['vrednost'] 




        # ----------------------------

        razdelilnik=self.object

        razdelilnik_data = {'razdelilnik_pk': razdelilnik.pk}

        self.request.session['razdelilnik_data'] = razdelilnik_data


        strosek_list = Strosek.objects\
            .filter(
                # filtriramo glede na stavbo
                racun__stavba=razdelilnik.stavba,
                # samo stroški, ki niso vezani na razdelilnik
                strosekrazdelilnik__isnull=True, 
                # filtriramo glede na mesec obracuna
                #datum_storitve_od__month__lte=razdelilnik.obdobje_obracuna_mesec,
                # zanimajo nas samo stroški, ki so del razdelilnika 
                #racun__davcna_klasifikacija=1
                )\
            .order_by(
                # zaradi regroup prikaza stroškov po vrsti stroška, je potreben ustrezen sort
                # sort po kontu - O...obratovanje
                'vrsta_stroska__skupina__skupina__skupina__zap_st',
                # sort po podkontu - O-TVZ... tekoče vzdrževanje
                'vrsta_stroska__skupina__skupina__zap_st',
                # sort po skupini vrste stroška - O-TVZ-02... Vzdrževalna dela
                'vrsta_stroska__skupina__zap_st',
                # sort po vrsti stroška - O-TVZ-02A... planirana vzdrževalna dela
                'vrsta_stroska__zap_st',
                )


        context['strosek_list'] = strosek_list






        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RAZDELILNIK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context



    def post(self, request, *args, **kwargs):

        #==========================================
        # FORMS
        #==========================================
        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        #==========================================
        # PRIDOBIMO PODATKE
        #==========================================

        # Reklamacija instance
        razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

        razdelilnik_data = {'razdelilnik': razdelilnik}

        request.session['razdelilnik_data'] = razdelilnik_data

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_detail")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=razdelilnik.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True

        #==========================================
        # UKAZI
        #==========================================

        # Arhiviranje dokumenta

        if arhiviranje_create_form_is_valid == True:

            Arhiviranje.objects.create_arhiviranje(
                razdelilnik=razdelilnik,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev
            return HttpResponseRedirect(reverse('moduli:reklamacije:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))


        # IF NOT VALID
        return render(
            request, self.template_name, {
                'object': razdelilnik,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )