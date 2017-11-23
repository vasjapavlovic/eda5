# Python

# Django
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Dogodek
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms import dogodek_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm





class DogodekCreateFromZahtevekView(UpdateView):
    model = Zahtevek
    template_name = "dogodki/dogodek/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(DogodekCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['dogodek_create_form'] = dogodek_forms.DogodekCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOGODEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        dogodek_create_form = dogodek_forms.DogodekCreateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        dogodek_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOGODEK_CREATE")

        # podatki o instanci
        if dogodek_create_form.is_valid():
            datum_dogodka = dogodek_create_form.cleaned_data['datum_dogodka']
            cas_dogodka = dogodek_create_form.cleaned_data['cas_dogodka']
            opis_dogodka = dogodek_create_form.cleaned_data['opis_dogodka']
            is_potrebna_prijava_policiji = dogodek_create_form.cleaned_data['is_potrebna_prijava_policiji']
            is_nastala_skoda = dogodek_create_form.cleaned_data['is_nastala_skoda']
            povzrocitelj = dogodek_create_form.cleaned_data['povzrocitelj']
            dogodek_create_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if dogodek_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo dogodek

            dogodek = Dogodek.objects.create_dogodek(
                datum_dogodka=datum_dogodka,
                cas_dogodka=cas_dogodka,
                opis_dogodka=opis_dogodka,
                is_potrebna_prijava_policiji=is_potrebna_prijava_policiji,
                is_nastala_skoda=is_nastala_skoda,
                povzrocitelj=povzrocitelj,
                zahtevek=zahtevek
            )


            # spremenimo status dogodka v reševanju
            dogodek.status = 3
            dogodek.save()

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'dogodek_create_form': dogodek_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class DogodekUpdateFromZahtevekView(UpdateView):
    model = Dogodek
    form_class = dogodek_forms.DogodekUpdateForm
    template_name = "dogodki/dogodek/update_dogodek.html"


    def get_context_data(self, *args, **kwargs):
        context = super(DogodekUpdateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOGODEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class DogodekListView(LoginRequiredMixin, ListView):
    model = Dogodek
    template_name = "dogodki/dogodek/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DogodekListView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="dogodek_list")
        context['modul_zavihek'] = modul_zavihek

        # my content
        context['dogodki_vresevanju'] = self.model.objects.status_vresevanju()
        context['dogodki_zakljuceno'] = self.model.objects.status_zakljuceno()

        return context


###########################################################
# Reklamacija Detail View
#----------------------------------------------------------
class DogodekDetailView(LoginRequiredMixin, DetailView):
    model = Dogodek
    template_name = "dogodki/dogodek/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DogodekDetailView, self).get_context_data(*args, **kwargs)

        # Arhiviranje
        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        # Zaznamek
        context['zaznamek_list'] = Zaznamek.objects.filter(dogodek=self.object.id).order_by('-datum', '-ura')

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="dogodek_detail")
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

        # Dogodek instance
        dogodek = Dogodek.objects.get(id=self.get_object().id)

        # user
        user = request.user

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="dogodek_detail")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=dogodek.zahtevek.oznaka)
            arhiviral = Oseba.objects.get(user=user)
            arhiviranje_create_form_is_valid = True

        #==========================================
        # UKAZI
        #==========================================

        # Arhiviranje dokumenta

        if arhiviranje_create_form_is_valid == True:

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


        # IF NOT VALID
        return render(
            request, self.template_name, {
                'object': dogodek,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )
