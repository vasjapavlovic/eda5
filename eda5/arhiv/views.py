from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Models
from .models import Arhiviranje, ArhivMesto
from eda5.delovninalogi.models import DelovniNalog
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba
from eda5.pomanjkljivosti.models import Pomanjkljivost
from eda5.povprasevanje.models import Povprasevanje
from eda5.razdelilnik.models import Razdelilnik
from eda5.reklamacije.models import Reklamacija
from eda5.sestanki.models import Sestanek
from eda5.skladisce.models import Dobava
from eda5.zahtevki.models import Zahtevek

# Forms
from .forms import ArhiviranjeZahtevekForm


class ArhiviranjeListView(ListView):
    model = Arhiviranje
    template_name = "arhiv/arhiviranje/list/base.html"



# POPUP
# dodatek za filtriranje prikazanega seznama
from eda5.core.views import FilteredListView
from .forms import ArhiviranjeSearchForm
class ArhiviranjePopUpListView(FilteredListView):
    model = Arhiviranje
    form_class= ArhiviranjeSearchForm
    template_name = "arhiv/arhiviranje/popup/popup_base.html"
    paginate_by = 10



class ArhiviranjeCreateFromZahtevek(DetailView):
    model = Zahtevek
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromZahtevek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")



        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                zahtevek=zahtevek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromReklamacija(DetailView):
    model = Reklamacija
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromReklamacija, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        reklamacija = Reklamacija.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=reklamacija.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                reklamacija=reklamacija,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:reklamacije:reklamacija_detail', kwargs={'pk': reklamacija.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromDelovniNalog(DetailView):
    model = DelovniNalog
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromDelovniNalog, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=delovninalog.opravilo.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                delovninalog=delovninalog,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )



class ArhiviranjeCreateFromDobava(DetailView):
    model = Dobava
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromDobava, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        dobava = Dobava.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka="DOBAVA")

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                dobava=dobava,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:skladisce:dobava_detail', kwargs={'pk': dobava.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )



class ArhiviranjeCreateFromSestanek(DetailView):
    model = Sestanek
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromSestanek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        sestanek = Sestanek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=sestanek.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                sestanek=sestanek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:sestanki:sestanek_detail', kwargs={'pk': sestanek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromPovprasevanje(DetailView):
    model = Povprasevanje
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromPovprasevanje, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        povprasevanje = Povprasevanje.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=povprasevanje.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                povprasevanje=povprasevanje,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': povprasevanje.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromRazdelilnik(DetailView):
    model = Razdelilnik
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromRazdelilnik, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=razdelilnik.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

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

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromDogodek(DetailView):
    model = Dogodek
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromDogodek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # dogodek
        dogodek = Dogodek.objects.get(id=self.get_object().id)

        # user
        user = request.user

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=dogodek.zahtevek.oznaka)
            arhiviral = Oseba.objects.get(user=user)
            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                dogodek=dogodek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:dogodki:dogodek_detail', kwargs={'pk': dogodek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class ArhiviranjeCreateFromPomanjkljivost(DetailView):
    model = Pomanjkljivost
    template_name = "arhiv/arhiviranje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ArhiviranjeCreateFromPomanjkljivost, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        arhiviranje_create_form = ArhiviranjeZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        arhiviranje_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        pomanjkljivost = Pomanjkljivost.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="arhiviranje_create")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=pomanjkljivost.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True
        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if arhiviranje_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Arhiviranje.objects.create_arhiviranje(
                pomanjkljivost=pomanjkljivost,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:pomanjkljivosti:pomanjkljivost_detail', kwargs={'pk': pomanjkljivost.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )
