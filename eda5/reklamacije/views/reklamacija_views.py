from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView


# Reklamacije
from ..models import Reklamacija
from ..forms import reklamacija_forms

# Moduli
from eda5.moduli.models import Zavihek

# Zahtevki
from eda5.zahtevki.models import Zahtevek


class ReklamacijaCreateFromZahtevekView(UpdateView):
	model = Zahtevek
	template_name = "reklamacije/reklamacija/create/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ReklamacijaCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['reklamacija_create_from_zahtevek_form'] = reklamacija_forms.ReklamacijaCreateFromZahtevekForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
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

	        # Izdelamo zaznamek

	        Reklamacija.objects.create_reklamacija(
	            oznaka=oznaka,
	            naziv=naziv,
	            datum=datum,
	            narocnik=narocnik,
	            izvajalec=izvajalec,
	            okvirni_strosek=okvirni_strosek,
	            zahtevek=zahtevek,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'reklamacija_create_from_zahtevek_form': reklamacija_create_from_zahtevek_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )