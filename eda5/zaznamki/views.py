from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse

from django.views.generic import DetailView, UpdateView



from .forms import ZaznamekUpdateForm, ZaznamekCreateForm
from .models import Zaznamek

# Moduli
from eda5.moduli.models import Zavihek

# Zahtevki
from eda5.zahtevki.models import Zahtevek


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
