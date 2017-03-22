from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Reklamacija
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms import reklamacija_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm


class ReklamacijaCreateFromZahtevekView(LoginRequiredMixin, UpdateView):
	model = Zahtevek
	template_name = "reklamacije/reklamacija/create/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ReklamacijaCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['reklamacija_create_from_zahtevek_form'] = reklamacija_forms.ReklamacijaCreateFromZahtevekForm

		modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_create")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    reklamacija_create_from_zahtevek_form = reklamacija_forms.ReklamacijaCreateFromZahtevekForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    reklamacija_create_from_zahtevek_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    zahtevek = Zahtevek.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if reklamacija_create_from_zahtevek_form.is_valid():
	        oznaka = reklamacija_create_from_zahtevek_form.cleaned_data['oznaka']
	        naziv = reklamacija_create_from_zahtevek_form.cleaned_data['naziv']
	        opis = reklamacija_create_from_zahtevek_form.cleaned_data['opis']
	        datum = reklamacija_create_from_zahtevek_form.cleaned_data['datum']
	        narocnik = reklamacija_create_from_zahtevek_form.cleaned_data['narocnik']
	        izvajalec = reklamacija_create_from_zahtevek_form.cleaned_data['izvajalec']
	        okvirni_strosek = reklamacija_create_from_zahtevek_form.cleaned_data['okvirni_strosek']
	        reklamacija_create_from_zahtevek_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if reklamacija_create_from_zahtevek_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo reklamacijo

	        reklamacija = Reklamacija.objects.create_reklamacija(
	            oznaka=oznaka,
	            naziv=naziv,
	            datum=datum,
	            narocnik=narocnik,
	            izvajalec=izvajalec,
	            okvirni_strosek=okvirni_strosek,
	            zahtevek=zahtevek,
	        )


	        # spremenimo status reklamacije v reševanju
	        reklamacija.status = 3
	        reklamacija.save()

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'reklamacija_create_from_zahtevek_form': reklamacija_create_from_zahtevek_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ReklamacijaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reklamacija
    form_class = reklamacija_forms.ReklamacijaUpdateForm
    template_name = "reklamacije/reklamacija/update/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReklamacijaUpdateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_create")
        context['modul_zavihek'] = modul_zavihek

        return context



class ReklamacijaListView(LoginRequiredMixin, ListView):
    model = Reklamacija
    template_name = "reklamacije/reklamacija/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReklamacijaListView, self).get_context_data(*args, **kwargs)

        # content
        context['reklamacije_vresevanju'] = self.model.objects.status_vresevanju()
        context['reklamacije_zakljucene'] = self.model.objects.status_zakljuceno()

        modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_list")
        context['modul_zavihek'] = modul_zavihek

        return context


###########################################################
# Reklamacija Detail View
#----------------------------------------------------------
class ReklamacijaDetailView(LoginRequiredMixin, DetailView):
    model = Reklamacija
    template_name = "reklamacije/reklamacija/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReklamacijaDetailView, self).get_context_data(*args, **kwargs)

        context['arhiviranje_create_form'] = ArhiviranjeZahtevekForm

        context['zaznamek_list'] = Zaznamek.objects.filter(reklamacija=self.object.id).order_by('-datum', '-ura')
        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_detail")
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
        reklamacija = Reklamacija.objects.get(id=self.get_object().id)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="reklamacija_detail")

        # Podatki za arhiviranje dokumenta
        if arhiviranje_create_form.is_valid():
            dokument = arhiviranje_create_form.cleaned_data['dokument']
            elektronski = arhiviranje_create_form.cleaned_data['elektronski']
            fizicni = arhiviranje_create_form.cleaned_data['fizicni']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka=reklamacija.zahtevek.oznaka)

            user = request.user
            arhiviral = Oseba.objects.get(user=user)

            arhiviranje_create_form_is_valid = True

        #==========================================
        # UKAZI
        #==========================================

        # Arhiviranje dokumenta

        if arhiviranje_create_form_is_valid == True:

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


        # IF NOT VALID
        return render(
            request, self.template_name, {
                'object': reklamacija,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
            	}
            )