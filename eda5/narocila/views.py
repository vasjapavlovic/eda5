from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.context_processors import csrf

from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView

from .forms import NarociloCreateIzbiraForm, NarociloSplosnoCreateForm, NarociloTelefonCreateForm
from .forms import NarociloDokumentCreateForm, NarociloDokumentUpdateForm
from .models import Narocilo, NarociloTelefon, NarociloDokument


from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Partner, Oseba
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

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        narocilo_splosno_form = NarociloSplosnoCreateForm(request.POST or None)
        narocilo_telefon_form = NarociloTelefonCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")

        if narocilo_telefon_form.is_valid():
            oseba = narocilo_telefon_form.cleaned_data['oseba']
            telefonska_stevilka = narocilo_telefon_form.cleaned_data['telefonska_stevilka']
            datum_klica = narocilo_telefon_form.cleaned_data['datum_klica']
            cas_klica = narocilo_telefon_form.cleaned_data['cas_klica']
            telefonsko_sporocilo = narocilo_telefon_form.cleaned_data['telefonsko_sporocilo']

            narocilo_telefon_data = NarociloTelefon.objects.create_narocilo_telefon(
                oseba=oseba,
                telefonska_stevilka=telefonska_stevilka,
                datum_klica=datum_klica,
                cas_klica=cas_klica,
                telefonsko_sporocilo=telefonsko_sporocilo,
            )
            narocilo_telefon = NarociloTelefon.objects.get(id=narocilo_telefon_data.pk)

        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_telefon_form': narocilo_telefon_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if narocilo_splosno_form.is_valid():
            narocnik = narocilo_splosno_form.cleaned_data['narocnik']
            izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
            oznaka = narocilo_splosno_form.cleaned_data['oznaka']
            predmet = narocilo_splosno_form.cleaned_data['predmet']
            datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
            datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
            vrednost = narocilo_splosno_form.cleaned_data['vrednost']

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

        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_telefon_form': narocilo_telefon_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk }))


# view called with ajax to reload the month drop down list
def reload_controls_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the year that the user has typed
    partner = request.POST['partner']

    # definiramo objekt
    partner = Partner.objects.get(id=partner)

    # izdelamo seznam oseb (id-ji)
    osebe = []
    for partner in partner.all():
        for oseba in partner.oseba_set.all():
            # vnesemov seznam, ki ga gradimo
            osebe.append(oseba.id)

    # osebe to display
    context['list_to_display'] = osebe

    return JsonResponse(context)


# class NarociloPogodbaCreateView(TemplateView):
#     template_name = "narocila/narocilo/create_pogodba.html"


class NarociloDetailView(DetailView):
    model = Narocilo
    template_name = 'narocila/narocilo/detail/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


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
            tip_dokumenta = narocilo_dokument_form.cleaned_data['tip_dokumenta']
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
                tip_dokumenta=tip_dokumenta,
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



# class NarociloDokumentCreateView(UpdateView):
#     model = Zahtevek
#     template_name = "narocila/narocilo/create_dokument.html"
#     fields = ('id', )

#     def get_context_data(self, *args, **kwargs):
#         context = super(NarociloDokumentCreateView, self).get_context_data(*args, **kwargs)

#         # narocila
#         context['narocilo_splosno_form'] = NarociloSplosnoCreateForm
#         context['narocilo_dokument_form'] = NarociloDokumentCreateForm
#         # moduli
#         modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
#         context['modul_zavihek'] = modul_zavihek

#         return context

#     def post(self, request, *args, **kwargs):

#         #############
#         ''' SETUP'''
#         #############
#         ''' Pridobimo zahtevek v katerem se naročilo izdeluje '''
#         zahtevek = Zahtevek.objects.get(id=self.get_object().id)
#         # narocilo
#         narocilo_splosno_form = NarociloSplosnoCreateForm(request.POST or None)
#         narocilo_dokument_form = NarociloDokumentCreateForm(request.POST or None)
#         # moduli
#         modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_CREATE_DOKUMENT")

#         #####################################
#         ''' PRIDOBITEV PODATKOV IZ FORMS'''
#         #####################################
#         if narocilo_splosno_form.is_valid():
#             narocnik = narocilo_splosno_form.cleaned_data['narocnik']
#             izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
#             oznaka = narocilo_splosno_form.cleaned_data['oznaka']
#             predmet = narocilo_splosno_form.cleaned_data['predmet']
#             datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
#             datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
#             vrednost = narocilo_splosno_form.cleaned_data['vrednost']


#             # create narocilo-splosno
#             narocilo_data = Narocilo.objects.create_narocilo(
#                 zahtevek=zahtevek,
#                 narocnik=narocnik,
#                 izvajalec=izvajalec,
#                 oznaka=oznaka,
#                 predmet=predmet,
#                 datum_narocila=datum_narocila,
#                 datum_veljavnosti=datum_veljavnosti,
#                 vrednost=vrednost,
#             )
#             narocilo = Narocilo.objects.get(id=narocilo_data.pk)


#         else:
#             return render(request, self.template_name, {
#                 'narocilo_splosno_form': narocilo_splosno_form,
#                 'narocilo_dokument_form': narocilo_dokument_form,
#                 'modul_zavihek': modul_zavihek,
#                 }
#             )

#         if narocilo_dokument_form.is_valid():
#             tip_dokumenta = narocilo_dokument_form.cleaned_data['tip_dokumenta']

#             # create narocilo-dokument
#             narocilo_dokument_data = NarociloDokument.objects.create_narocilo_dokument(
#                 tip_dokumenta=tip_dokumenta,
#                 narocilo=narocilo,
#             )

#             narocilo_dokument = Narocilo.objects.get(id=narocilo_dokument_data.pk)

#         else:
#             return render(request, self.template_name, {
#                 'narocilo_splosno_form': narocilo_splosno_form,
#                 'narocilo_dokument_form': narocilo_dokument_form,
#                 'modul_zavihek': modul_zavihek,
#                 }
#             )

#         return HttpResponseRedirect(reverse('moduli:narocila:narocilo_update_dokument', kwargs={'pk': narocilo_dokument.pk }))

        ################################
        ''' IZDELAVA VNOSA V BAZI '''
        ################################



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

    
            