from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Sestanek, Tocka, Sklep, Tema
from eda5.moduli.models import Zavihek
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek


# Forms
from ..forms import sestanek_forms


class SestanekCreateFromZahtevekView(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    template_name = "sestanki/sestanek/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(SestanekCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['sestanek_create_from_zahtevek_form'] = sestanek_forms.SestanekCreateFromZahtevekForm
        context['sestanek_prisotni_update_form'] = sestanek_forms.SestanekPrisotniUpdateForm

        modul_zavihek = Zavihek.objects.get(oznaka="sestanek_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        sestanek_create_from_zahtevek_form = sestanek_forms.SestanekCreateFromZahtevekForm(request.POST or None)
        sestanek_prisotni_update_form = sestanek_forms.SestanekPrisotniUpdateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        sestanek_create_from_zahtevek_form_is_valid = False
        sestanek_prisotni_update_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o sestanku
        if sestanek_create_from_zahtevek_form.is_valid():
            oznaka = sestanek_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = sestanek_create_from_zahtevek_form.cleaned_data['naziv']
            opis = sestanek_create_from_zahtevek_form.cleaned_data['opis']
            datum = sestanek_create_from_zahtevek_form.cleaned_data['datum']
            sklicatelj = sestanek_create_from_zahtevek_form.cleaned_data['sklicatelj']
            sestanek_create_from_zahtevek_form_is_valid = True

        # podatki o prisotnih
        if sestanek_prisotni_update_form.is_valid():
            prisotni = sestanek_prisotni_update_form.cleaned_data['prisotni']
            sestanek_prisotni_update_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if sestanek_create_from_zahtevek_form_is_valid == True and sestanek_prisotni_update_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo sestanek

            sestanek = Sestanek.objects.create_sestanek(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                datum=datum,
                sklicatelj=sklicatelj,
                zahtevek=zahtevek,
            )

            # instanco izdelanega opravila shranimo za nadaljno uporabo

            sestanek_object = Sestanek.objects.get(id=sestanek.pk)

            # dodelimo podatke o prisotnih

            sestanek_object.prisotni = prisotni
            sestanek_object.save()

            # spremenimo status reklamacije v reševanju
            sestanek.status = 3
            sestanek.save()

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'sestanek_create_from_zahtevek_form': sestanek_create_from_zahtevek_form,
                'sestanek_prisotni_update_form': sestanek_prisotni_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class SestanekUpdateView(LoginRequiredMixin, UpdateView):
    model = Sestanek
    form_class = sestanek_forms.SestanekUpdateForm
    template_name = "sestanki/sestanek/update/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SestanekUpdateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="sestanek_create")
        context['modul_zavihek'] = modul_zavihek

        return context



class SestanekListView(LoginRequiredMixin, ListView):
    model = Sestanek
    template_name = "sestanki/sestanek/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SestanekListView, self).get_context_data(*args, **kwargs)

        # content


        modul_zavihek = Zavihek.objects.get(oznaka="sestanek_list")
        context['modul_zavihek'] = modul_zavihek

        return context


###########################################################
# Sestanek Detail View
#----------------------------------------------------------
class SestanekDetailView(LoginRequiredMixin, DetailView):
    model = Sestanek
    template_name = "sestanki/sestanek/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SestanekDetailView, self).get_context_data(*args, **kwargs)

        context['zaznamek_list'] = Zaznamek.objects.filter(sestanek=self.object.id).order_by('-datum', '-ura')

        # točke dnevnega reda sestanka
        tocka_list = Tocka.objects.filter(sestanek=self.object.id).order_by('oznaka',)
        context['tocka_list'] = tocka_list

        # sklepi sestanka
        sklep_list = Sklep.objects.filter(tocka__sestanek=self.object.id).order_by('tocka__oznaka', 'oznaka',)
        context['sklep_list'] = sklep_list


        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="sestanek_detail")
        context['modul_zavihek'] = modul_zavihek

        return context