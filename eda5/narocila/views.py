from django.contrib import messages
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView

# Delovninalogi
from .forms import NarociloCreateIzbiraForm, NarociloSplosnoCreateForm, NarociloTelefonCreateForm
from .forms import NarociloDokumentCreateForm, NarociloDokumentUpdateForm
from .models import Narocilo, NarociloTelefon, NarociloDokument


# Arhiv
from eda5.arhiv.models import Arhiviranje

# Moduli
from eda5.moduli.models import Zavihek

# Partnerji
from eda5.partnerji.models import Partner, Oseba

# Zahtevki
from eda5.zahtevki.models import Zahtevek


class NarocilaHomeView(TemplateView):
    template_name = "narocila/home.html"


class NarociloListView(ListView):

    model = Narocilo
    template_name = "narocila/narocilo/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloListView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class NarociloCreateIzbiraView(UpdateView):
    model = Zahtevek
    template_name = "narocila/narocilo/create_izbira.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloCreateIzbiraView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['narocilo_izbira_create_form'] = NarociloCreateIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        narocilo_izbira_create_form = NarociloCreateIzbiraForm(request.POST or None)

        if narocilo_izbira_create_form.is_valid():

            vrsta_narocila = narocilo_izbira_create_form.cleaned_data['vrsta_narocila']

            # naročilo telefon
            if vrsta_narocila == '1':
                return HttpResponseRedirect(reverse('moduli:narocila:narocilo_create_telefon', kwargs={'pk': zahtevek.pk}))

            # naročilo dokument
            if vrsta_narocila == '2':
                return HttpResponseRedirect(reverse('moduli:narocila:narocilo_create_dokument', kwargs={'pk': zahtevek.pk}))



class NarociloTelefonCreateView(UpdateView):
    model = Zahtevek
    template_name = "narocila/narocilo/create_telefon.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloTelefonCreateView, self).get_context_data(*args, **kwargs)
        context['narocilo_splosno_form'] = NarociloSplosnoCreateForm
        context['narocilo_telefon_form'] = NarociloTelefonCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        #############
        ''' SETUP'''
        #############
        ''' Pridobimo zahtevek v katerem se naročilo izdeluje '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # Naročila
        narocilo_splosno_form = NarociloSplosnoCreateForm(request.POST or None)
        narocilo_telefon_form = NarociloTelefonCreateForm(request.POST or None)

        # Moduli
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")


        #####################################
        ''' PRIDOBITEV PODATKOV IZ FORMS'''
        #####################################

        # forms so na začetku neustrezno izpolnjene
        narocilo_telefon_form_is_valid = False
        narocilo_splosno_form_is_valid = False

        if narocilo_telefon_form.is_valid():
            dogovor_text = narocilo_telefon_form.cleaned_data['dogovor_text']
            dogovor_date = narocilo_telefon_form.cleaned_data['dogovor_date']
            dogovor_time = narocilo_telefon_form.cleaned_data['dogovor_time']
            dogovor_person = narocilo_telefon_form.cleaned_data['dogovor_person']
            dogovor_phonenumber = narocilo_telefon_form.cleaned_data['dogovor_phonenumber']
            narocilo_telefon_form_is_valid = True

        if narocilo_splosno_form.is_valid():
            narocnik = narocilo_splosno_form.cleaned_data['narocnik']
            izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
            oznaka = narocilo_splosno_form.cleaned_data['oznaka']
            predmet = narocilo_splosno_form.cleaned_data['predmet']
            datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
            datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
            vrednost = narocilo_splosno_form.cleaned_data['vrednost']
            narocilo_splosno_form_is_valid = True


        ################################
        ''' IZDELAVA VNOSA V BAZI '''
        ################################
        if narocilo_telefon_form_is_valid == True and narocilo_splosno_form_is_valid == True:

            narocilo_telefon_data = NarociloTelefon.objects.create_narocilo_telefon(
                dogovor_text=dogovor_text,
                dogovor_date=dogovor_date,
                dogovor_time=dogovor_time,
                dogovor_person=dogovor_person,
                dogovor_phonenumber=dogovor_phonenumber,
            )

            narocilo_telefon = NarociloTelefon.objects.get(id=narocilo_telefon_data.pk)

            Narocilo.objects.create_narocilo(
                zahtevek=zahtevek,
                narocilo_telefon=narocilo_telefon,
                narocnik=narocnik,
                izvajalec=izvajalec,
                oznaka=oznaka,
                predmet=predmet,
                datum_narocila=datum_narocila,
                datum_veljavnosti=datum_veljavnosti,
                vrednost=vrednost,
            )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk }))


        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_telefon_form': narocilo_telefon_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class NarociloDokumentCreateView(UpdateView):
    model = Zahtevek
    template_name = "narocila/narocilo/create_dokument.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloDokumentCreateView, self).get_context_data(*args, **kwargs)

        # narocila
        context['narocilo_splosno_form'] = NarociloSplosnoCreateForm
        context['narocilo_dokument_form'] = NarociloDokumentCreateForm
        # moduli
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        #############
        ''' SETUP'''
        #############
        ''' Pridobimo zahtevek v katerem se naročilo izdeluje '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)
        # narocilo
        narocilo_splosno_form = NarociloSplosnoCreateForm(request.POST or None)
        narocilo_dokument_form = NarociloDokumentCreateForm(request.POST or None)
        # moduli
        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_CREATE_DOKUMENT")

        #####################################
        ''' PRIDOBITEV PODATKOV IZ FORMS'''
        #####################################

        # forms so na začetku neustrezno izpolnjene
        narocilo_splosno_form_is_valid = False
        narocilo_dokument_form_is_valid = False

        if narocilo_splosno_form.is_valid():
            narocnik = narocilo_splosno_form.cleaned_data['narocnik']
            izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
            oznaka = narocilo_splosno_form.cleaned_data['oznaka']
            predmet = narocilo_splosno_form.cleaned_data['predmet']
            datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
            datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
            vrednost = narocilo_splosno_form.cleaned_data['vrednost']
            narocilo_splosno_form_is_valid = True

        if narocilo_dokument_form.is_valid():
            vrsta_dokumenta = narocilo_dokument_form.cleaned_data['vrsta_dokumenta']
            
            # VALIDACIJE **************************************************
            # Validacija 01
            # Če izbrane vrste dokumentov ni likvidiranih v zahtevku ne pusti naprej

            # pridobimo isntanco arhiviranja za dostopanje do dokumentov, 
            # ki so arhivirani pod zahtevkom
            arhiviranje_zahtevek = Arhiviranje.objects.filter(zahtevek=zahtevek)

            # pridobimo število izranih vrst dokumentov likvidiranih v zahtevku
            st_izbranih_vrst_dokumentov_likvidiranih_v_zahtevku = arhiviranje_zahtevek.filter(dokument__vrsta_dokumenta=vrsta_dokumenta).count()

            if st_izbranih_vrst_dokumentov_likvidiranih_v_zahtevku == 0:
                # sporočilo uporabniku
                messages.error(request, 'Zahtevek nima nobenega dokumenta s pripadajočo izbrano vrsto dokumenta.')
                # preusmeritev na obstoječi zahtevek brez vnosa
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk }))

            # KONEC VALIDACIJE ***********************************************
            narocilo_dokument_form_is_valid = True

        ################################
        ''' IZDELAVA VNOSA V BAZI '''
        ################################
        if narocilo_splosno_form_is_valid is True and narocilo_dokument_form_is_valid is True:

            # create narocilo-splosno
            narocilo_data = Narocilo.objects.create_narocilo(
                zahtevek=zahtevek,
                narocnik=narocnik,
                izvajalec=izvajalec,
                oznaka=oznaka,
                predmet=predmet,
                datum_narocila=datum_narocila,
                datum_veljavnosti=datum_veljavnosti,
                vrednost=vrednost,
            )
            narocilo = Narocilo.objects.get(id=narocilo_data.pk)

            # create narocilo-dokument
            narocilo_dokument_data = NarociloDokument.objects.create_narocilo_dokument(
                vrsta_dokumenta=vrsta_dokumenta,
                narocilo=narocilo,
            )

            ''' pridobimo objekt NarociloDokument, ki ga rabimo, da izvedemo update in dodamo dokument'''
            narocilo_dokument = Narocilo.objects.get(id=narocilo_dokument_data.pk)


            return HttpResponseRedirect(reverse('moduli:narocila:narocilo_update_dokument', kwargs={'pk': narocilo_dokument.pk }))

        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_dokument_form': narocilo_dokument_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class NarociloDetailView(DetailView):
    model = Narocilo
    template_name = 'narocila/narocilo/detail/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class NarociloDokumentUpdateView(UpdateView):

    model = NarociloDokument
    form_class = NarociloDokumentUpdateForm
    template_name = "narocila/narocilo/update_dokument.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloDokumentUpdateView, self).get_context_data(*args, **kwargs)

        # moduli
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_success_url(self, **kwargs):
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.object.narocilo.zahtevek.pk })




# view called with ajax to reload the month drop down list
def reload_controls_narocilo_osebe_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the year that the user has typed
    # partner = request.POST['partner'] <-- ne dela
    # definiramo objekt
    partner = Partner.objects.get(id=105)
    print(partner)
    # izdelamo seznam oseb (id-ji)
    osebe = []
    for oseba in partner.oseba_set.all():
        # vnesemov seznam, ki ga gradimo
        osebe.append(oseba.id)

    # osebe to display
    context['list_to_display'] = osebe

    return JsonResponse(context)