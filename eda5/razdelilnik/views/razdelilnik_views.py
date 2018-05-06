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
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms.razdelilnik_forms import RazdelilnikSearchForm, RazdelilnikCreateFromZahtevekForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.reports.forms.forms import FormatForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse



class RazdelilnikCreateFromZahtevekView(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    template_name = "razdelilnik/razdelilnik/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(RazdelilnikCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['razdelilnik_create_from_zahtevek_form'] = RazdelilnikCreateFromZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="razdelilnik_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        razdelilnik_create_from_zahtevek_form = RazdelilnikCreateFromZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        razdelilnik_create_from_zahtevek_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="razdelilnik_create")

        # podatki o opravilu
        if razdelilnik_create_from_zahtevek_form.is_valid():
            oznaka = razdelilnik_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = razdelilnik_create_from_zahtevek_form.cleaned_data['naziv']
            stavba = razdelilnik_create_from_zahtevek_form.cleaned_data['stavba']
            obdobje_obracuna_leto = razdelilnik_create_from_zahtevek_form.cleaned_data['obdobje_obracuna_leto']
            obdobje_obracuna_mesec = razdelilnik_create_from_zahtevek_form.cleaned_data['obdobje_obracuna_mesec']

            razdelilnik_create_from_zahtevek_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if razdelilnik_create_from_zahtevek_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo reklamacijo

            razdelilnik = Razdelilnik.objects.create_razdelilnik(
                oznaka=oznaka,
                naziv=naziv,
                stavba=stavba,
                obdobje_obracuna_leto=obdobje_obracuna_leto,
                obdobje_obracuna_mesec=obdobje_obracuna_mesec,
                zahtevek=zahtevek,
            )

            # spremenimo status razdelilnika v reševanju
            razdelilnik.status = 3
            razdelilnik.save()

            # izvedemo preusmeritev
            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'razdelilnik_create_from_zahtevek_form': razdelilnik_create_from_zahtevek_form,
                'modul_zavihek': modul_zavihek,
                }
            )

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


        # Zavihek
        #################################################
        modul_zavihek = Zavihek.objects.get(oznaka="RAZDELILNIK_DETAIL")
        context['modul_zavihek'] = modul_zavihek


        # ARHIVIRANJE
        #################################################
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm


        # ZAZNAMKI
        #################################################
        context['zaznamek_list'] = Zaznamek.objects.filter(razdelilnik=self.object.id).order_by('-datum', '-ura')

        # Format - izvoz
        context['format_form'] = FormatForm


        # OSTALO
        #################################################

        # instanca razdelilnika
        razdelilnik=self.object
        # podatek o instanci spravimo v sessions za nadaljno uporabo
        # potrebujemo ga za izdelavo vezave stroška na obstoječ razdelilnik
        razdelilnik_data = {'razdelilnik_pk': razdelilnik.pk}
        self.request.session['razdelilnik_data'] = razdelilnik_data

        # Pripravimo seznam stroškov, ki ga bomo prikazali
        # kot opcijo za vezavo na razdelilnik
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


        # Pripravimo seznam Stroškov vezanih na razdelilnik
        strosekrazdelilnik_list = StrosekRazdelilnik.objects\
            .filter(razdelilnik=self.object.id)\
            .order_by(
                # zaradi regroup prikaza stroškov po vrsti stroška, je potreben ustrezen sort
                # sort po kontu - O...obratovanje
                'strosek__vrsta_stroska__skupina__skupina__skupina__zap_st',
                # sort po podkontu - O-TVZ... tekoče vzdrževanje
                'strosek__vrsta_stroska__skupina__skupina__zap_st',
                # sort po skupini vrste stroška - O-TVZ-02... Vzdrževalna dela
                'strosek__vrsta_stroska__skupina__zap_st',
                # sort po vrsti stroška - O-TVZ-02A... planirana vzdrževalna dela
                'strosek__vrsta_stroska__zap_st',
                )

        strosekrazdelilnik_nerazdeljeni = strosekrazdelilnik_list\
            .filter(is_razdeljen=False)

        strosekrazdelilnik_razdeljeni = strosekrazdelilnik_list\
            .filter(is_razdeljen=True)

        # seštevek vrednosti BREZ DDV za vse stroške iz seznama zgoraj
        vrednost_razdelilnik_osnova = strosekrazdelilnik_list\
            .aggregate(vrednost=Sum('strosek__osnova'))

        # seštevek vrednosti neobdavčenega stroška
        vrednost_razdelilnik_ddvbrez = strosekrazdelilnik_list\
            .filter(strosek__stopnja_ddv=0)\
            .aggregate(vrednost=Sum('strosek__osnova')*1)
        # v primeru, da neobdavčenega stroška ni,
        # vrni vrednost = 0
        if vrednost_razdelilnik_ddvbrez['vrednost'] == None:
            vrednost_razdelilnik_ddvbrez['vrednost'] = 0

        # seštevek vrednosti stroška po nižji stopnji ddv
        vrednost_razdelilnik_ddvnizja = strosekrazdelilnik_list\
            .filter(strosek__stopnja_ddv=1)\
            .aggregate(vrednost=Sum('strosek__osnova')*1.095)
        # v primeru, da stroška po nižji stopnji ni,
        # vrni vrednost = 0
        if vrednost_razdelilnik_ddvnizja['vrednost'] == None:
            vrednost_razdelilnik_ddvnizja['vrednost'] = 0

        # seštevek vrednosti po višji stopnji ddv
        vrednost_razdelilnik_ddvvisja = strosekrazdelilnik_list\
            .filter(strosek__stopnja_ddv=2)\
            .aggregate(vrednost=Sum('strosek__osnova')*1.22)
        # v primeru, da stroška po višji stopnji ni,
        # vrni vrednost = 0
        if vrednost_razdelilnik_ddvvisja['vrednost'] == None:
            vrednost_razdelilnik_ddvvisja['vrednost'] = 0

        # seštevek vrednosti Z DDV za vse stroške iz seznama zgoraj
        vrednost_razdelilnik_zddv = vrednost_razdelilnik_ddvbrez['vrednost'] + \
            vrednost_razdelilnik_ddvnizja['vrednost'] + vrednost_razdelilnik_ddvvisja['vrednost']


        # Izpišemo v context za prikaz
        context['strosekrazdelilnik_list'] = strosekrazdelilnik_list
        context['strosekrazdelilnik_nerazdeljeni'] = strosekrazdelilnik_nerazdeljeni
        context['strosekrazdelilnik_razdeljeni'] = strosekrazdelilnik_razdeljeni
        context['vrednost_razdelilnik_osnova'] = vrednost_razdelilnik_osnova
        context['vrednost_razdelilnik_ddvbrez'] = vrednost_razdelilnik_ddvbrez
        context['vrednost_razdelilnik_ddvnizja'] = vrednost_razdelilnik_ddvnizja
        context['vrednost_razdelilnik_ddvvisja'] = vrednost_razdelilnik_ddvvisja
        context['vrednost_razdelilnik_zddv'] = vrednost_razdelilnik_zddv
        context['strosek_list'] = strosek_list

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################
        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)
        format_form = FormatForm(request.POST or None)


        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False
        format_form_is_valid = True

        #==========================================
        # PRIDOBIMO PODATKE
        #==========================================

        # instanca razdelilnika
        razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

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
            return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))


        if format_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # iz instance pridobimo željene podatke
            # ki jih bomo uporabili v izpisu

            # Pripravimo seznam Stroškov vezanih na razdelilnik
            strosekrazdelilnik_list = StrosekRazdelilnik.objects\
                .filter(razdelilnik=razdelilnik)\
                .order_by(
                    # zaradi regroup prikaza stroškov po vrsti stroška, je potreben ustrezen sort
                    # sort po kontu - O...obratovanje
                    'strosek__vrsta_stroska__skupina__skupina__skupina__zap_st',
                    # sort po podkontu - O-TVZ... tekoče vzdrževanje
                    'strosek__vrsta_stroska__skupina__skupina__zap_st',
                    # sort po skupini vrste stroška - O-TVZ-02... Vzdrževalna dela
                    'strosek__vrsta_stroska__skupina__zap_st',
                    # sort po vrsti stroška - O-TVZ-02A... planirana vzdrževalna dela
                    'strosek__vrsta_stroska__zap_st',
                    # sort po številki računa
                    'strosek__racun__oznaka',
                    # sort po številki stroška
                    'strosek__oznaka',
                    )


            # seštevek vrednosti BREZ DDV za vse stroške iz seznama zgoraj
            vrednost_razdelilnik_osnova = strosekrazdelilnik_list\
                .aggregate(vrednost=Sum('strosek__osnova'))

            # seštevek vrednosti neobdavčenega stroška
            vrednost_razdelilnik_ddvbrez = strosekrazdelilnik_list\
                .filter(strosek__stopnja_ddv=0)\
                .aggregate(vrednost=Sum('strosek__osnova')*1)
            # v primeru, da neobdavčenega stroška ni,
            # vrni vrednost = 0
            if vrednost_razdelilnik_ddvbrez['vrednost'] == None:
                vrednost_razdelilnik_ddvbrez['vrednost'] = 0

            # seštevek vrednosti stroška po nižji stopnji ddv
            vrednost_razdelilnik_ddvnizja = strosekrazdelilnik_list\
                .filter(strosek__stopnja_ddv=1)\
                .aggregate(vrednost=Sum('strosek__osnova')*1.095)
            # v primeru, da stroška po nižji stopnji ni,
            # vrni vrednost = 0
            if vrednost_razdelilnik_ddvnizja['vrednost'] == None:
                vrednost_razdelilnik_ddvnizja['vrednost'] = 0

            # seštevek vrednosti po višji stopnji ddv
            vrednost_razdelilnik_ddvvisja = strosekrazdelilnik_list\
                .filter(strosek__stopnja_ddv=2)\
                .aggregate(vrednost=Sum('strosek__osnova')*1.22)
            # v primeru, da stroška po višji stopnji ni,
            # vrni vrednost = 0
            if vrednost_razdelilnik_ddvvisja['vrednost'] == None:
                vrednost_razdelilnik_ddvvisja['vrednost'] = 0

            # seštevek vrednosti Z DDV za vse stroške iz seznama zgoraj
            vrednost_razdelilnik_zddv = vrednost_razdelilnik_ddvbrez['vrednost'] + \
                vrednost_razdelilnik_ddvnizja['vrednost'] + vrednost_razdelilnik_ddvvisja['vrednost']

            self.strosekrazdelilnik_list = strosekrazdelilnik_list
            self.vrednost_razdelilnik_osnova = vrednost_razdelilnik_osnova
            self.vrednost_razdelilnik_ddvbrez = vrednost_razdelilnik_ddvbrez
            self.vrednost_razdelilnik_ddvnizja = vrednost_razdelilnik_ddvnizja
            self.vrednost_razdelilnik_ddvvisja = vrednost_razdelilnik_ddvvisja
            self.vrednost_razdelilnik_zddv = vrednost_razdelilnik_zddv

            # stavba
            self.stavba = razdelilnik.stavba
            # obdobje razdelilnika
            self.obdobje_leto = razdelilnik.obdobje_obracuna_leto
            self.obdobje_mesec = razdelilnik.obdobje_obracuna_mesec

            izpis_data = {
                'strosekrazdelilnik_list': strosekrazdelilnik_list,
                'vrednost_razdelilnik_osnova': vrednost_razdelilnik_osnova,
                'vrednost_razdelilnik_ddvbrez': vrednost_razdelilnik_ddvbrez,
                'vrednost_razdelilnik_ddvnizja': vrednost_razdelilnik_ddvnizja,
                'vrednost_razdelilnik_ddvvisja': vrednost_razdelilnik_ddvvisja,
                'vrednost_razdelilnik_zddv': vrednost_razdelilnik_zddv,
                'stavba': self.stavba,
                'obdobje_leto': self.obdobje_leto,
                'obdobje_mesec': self.obdobje_mesec,
            }

            # izdelamo izpis
            filename = fill_template(
                # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                'obrazci/razdelilnik/seznam_stroskov_po_razdelilniku.ods',
                # podatki za uporabo v oblikovni datoteki
                izpis_data,
                output_format="xlsx"
            )

            visible_filename = '{}.{}'.format(razdelilnik.oznaka ,"xlsx")

            return FileResponse(filename, visible_filename)

        # IF NOT VALID
        return render(
            request, self.template_name, {
                'object': razdelilnik,
                'arhiviranje_create_form': arhiviranje_create_form,
                'format_form': format_form,
                'modul_zavihek': modul_zavihek,
                }
            )
