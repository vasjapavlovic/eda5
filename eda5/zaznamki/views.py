
# Django
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView, UpdateView

# Models
from .models import Zaznamek
from eda5.delovninalogi.models import DelovniNalog
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.povprasevanje.models import Povprasevanje
from eda5.razdelilnik.models import Razdelilnik
from eda5.reklamacije.models import Reklamacija
from eda5.sestanki.models import Sestanek
from eda5.skladisce.models import Dobava
from eda5.zahtevki.models import Zahtevek

# Forms
from .forms import ZaznamekUpdateForm, ZaznamekCreateForm


class ZaznamekUpdateFromZahtevekView(UpdateView):
    model = Zaznamek
    form_class = ZaznamekUpdateForm
    template_name = "zaznamki/zaznamek/update.html"


class ZaznamekCreateFromZahtevek(DetailView):
	model = Zahtevek
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromZahtevek, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    zahtevek = Zahtevek.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            zahtevek=zahtevek,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromReklamacija(DetailView):
	model = Reklamacija
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromReklamacija, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    reklamacija = Reklamacija.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            reklamacija=reklamacija,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:reklamacije:reklamacija_detail', kwargs={'pk': reklamacija.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromDelovniNalog(DetailView):
	model = DelovniNalog
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromDelovniNalog, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            delovninalog=delovninalog,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )



class ZaznamekCreateFromDobava(DetailView):
	model = Dobava
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromDobava, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    dobava = Dobava.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            dobava=dobava,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:skladisce:dobava_detail', kwargs={'pk': dobava.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromSestanek(DetailView):
	model = Sestanek
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromSestanek, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    sestanek = Sestanek.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            sestanek=sestanek,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:sestanki:sestanek_detail', kwargs={'pk': sestanek.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromPovprasevanje(DetailView):
	model = Povprasevanje
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromPovprasevanje, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    povprasevanje = Povprasevanje.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            povprasevanje=povprasevanje,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': povprasevanje.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromRazdelilnik(DetailView):
	model = Razdelilnik
	template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
	fields = ('id', )


	def get_context_data(self, *args, **kwargs):
		context = super(ZaznamekCreateFromRazdelilnik, self).get_context_data(*args, **kwargs)

		# zahtevek
		context['zaznamek_create_form'] = ZaznamekCreateForm

		modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
		context['modul_zavihek'] = modul_zavihek

		return context

	def post(self, request, *args, **kwargs):

	    # ====================================
	    # FORMS
	    # ====================================

	    zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

	    ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
	    Pomembno zaradi načina struktura View-ja '''

	    zaznamek_create_form_is_valid = False

	    ###########################################################################
	    # PRIDOBIMO PODATKE
	    ###########################################################################

	    # zahtevek
	    razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

	    # zavihek
	    modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

	    # podatki o opravilu
	    if zaznamek_create_form.is_valid():
	        tekst = zaznamek_create_form.cleaned_data['tekst']
	        datum = zaznamek_create_form.cleaned_data['datum']
	        ura = zaznamek_create_form.cleaned_data['ura']
	        zaznamek_create_form_is_valid = True

	    ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
	    izvrši spodnje ukaze '''

	    if zaznamek_create_form_is_valid == True:
	        ###########################################################################
	        # UKAZI
	        ###########################################################################

	        # Izdelamo zaznamek

	        Zaznamek.objects.create_zaznamek(
	        	tekst=tekst,
	            datum=datum,
	            ura=ura,
	            razdelilnik=razdelilnik,
	        )

	        # izvedemo preusmeritev

	        return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))

	    # če zgornji formi niso ustrezno izpolnjeni

	    else:
	        return render(request, self.template_name, {
	            'zaznamek_create_form': zaznamek_create_form,
	            'modul_zavihek': modul_zavihek,
	            }
	        )


class ZaznamekCreateFromDogodek(DetailView):
    model = Dogodek
    template_name = "zaznamki/zaznamek/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(ZaznamekCreateFromDogodek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['zaznamek_create_form'] = ZaznamekCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        zaznamek_create_form = ZaznamekCreateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        zaznamek_create_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        dogodek = Dogodek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o opravilu
        if zaznamek_create_form.is_valid():
            tekst = zaznamek_create_form.cleaned_data['tekst']
            datum = zaznamek_create_form.cleaned_data['datum']
            ura = zaznamek_create_form.cleaned_data['ura']
            zaznamek_create_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if zaznamek_create_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo zaznamek

            Zaznamek.objects.create_zaznamek(
                tekst=tekst,
                datum=datum,
                ura=ura,
                dogodek=dogodek,
            )

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:dogodki:dogodek_detail', kwargs={'pk': dogodek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'zaznamek_create_form': zaznamek_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )
