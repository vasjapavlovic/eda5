
from django.db import transaction
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import UpdateView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse



# Mixins
from braces.views import LoginRequiredMixin

# Models
from .models import Aktivnost
from .models import KontrolaSkupina
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect
from .models import KontrolaVrednost
from eda5.deli.models import ProjektnoMesto
from eda5.delovninalogi.models import DelovniNalog
from eda5.delovninalogi.models import Opravilo
from eda5.moduli.models import Zavihek


# Forms
from .forms import AktivnostCreateForm
from .forms import KontrolaVrednostUpdateFormSetOblika01
from .forms import KontrolaVrednostUpdateFormSetOblika02




# class KontrolniListSpecifikacijaCreateView(LoginRequiredMixin, UpdateView):
#     '''
#     View za izdelavo specifikacije kontrolnega lista iz OPRAVILA
#     '''
#
#     model = Opravilo
#     template_name = "kontrolnilist/create.html"
#     fields = ('id', )
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(KontrolniListSpecifikacijaCreateView, self).get_context_data(*args, **kwargs)
#
#         opravilo = Opravilo.objects.get(id=self.object.id)
#         context['opravilo'] = opravilo
#
#         if self.request.POST:
#             context['aktivnost_create_form'] = AktivnostCreateForm(self.request.POST)
#             context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(self.request.POST)
#         else:
#             context['aktivnost_create_form'] = AktivnostCreateForm()
#             context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet()
#
#
#         # # Zavihek
#         # modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
#         # context['modul_zavihek'] = modul_zavihek
#
#         return context
#
#
#     def post(self, request, *args, **kwargs):
#
#         opravilo = Opravilo.objects.get(pk=self.get_object().pk)
#
#         aktivnost_create_form = AktivnostCreateForm(self.request.POST)
#         kontrolni_list_create_formset = KontrolaSpecifikacijaFormSet(self.request.POST)
#
#
#         if aktivnost_create_form.is_valid():
#             # transaction.atomic() --> če je karkoli narobe se stanje v bazi povrne v prvotno stanje
#             with transaction.atomic():
#                 aktivnost_create_form.instance.opravilo = opravilo
#                 aktivnost_create_form_saved = aktivnost_create_form.save()
#
#                 if kontrolni_list_create_formset.is_valid():
#                     kontrolni_list_create_formset.instance = aktivnost_create_form_saved
#                     kontrolni_list_create_formset.save()
#
#             return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk}))
#
#
#         else:
#             return render(
#                 request,
#                 self.template_name,
#                 {
#                 'aktivnost_create_form': aktivnost_create_form,
#                 'kontrolni_list_create_formset': kontrolni_list_create_formset,
#                 },
#             )


class AktivnostSoftDeleteView(LoginRequiredMixin, UpdateView):
    '''
    Status aktivnosti spremenimo v "izbirsano"
    '''
    model = Aktivnost
    template_name = "kontrolnilist/aktivnost/soft_delete.html"
    fields = ('id', )


    def post(self, request, *args, **kwargs):

        akt = Aktivnost.objects.get(id=self.get_object().id)
        akt.status = 5
        akt.save()

        return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': akt.opravilo.pk}))




class KontrolniListAktivnostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    View za update aktivnosti
    '''

    model = Aktivnost
    template_name = "kontrolnilist/aktivnost/update.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListAktivnostUpdateView, self).get_context_data(*args, **kwargs)

        aktivnost = Aktivnost.objects.get(id=self.object.id)
        context['aktivnost'] = aktivnost

        if self.request.POST:
            context['aktivnost_create_form'] = AktivnostCreateForm(self.request.POST, instance=aktivnost)
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(self.request.POST, instance=aktivnost)
        else:
            context['aktivnost_create_form'] = AktivnostCreateForm(instance=aktivnost)
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(instance=aktivnost)


        # # Zavihek
        # modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        # context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        aktivnost = Aktivnost.objects.get(pk=self.get_object().pk)

        aktivnost_create_form = AktivnostCreateForm(self.request.POST, instance=aktivnost)
        kontrolni_list_create_formset = KontrolaSpecifikacijaFormSet(self.request.POST, instance=aktivnost)


        if aktivnost_create_form.is_valid():
            # transaction.atomic() --> če je karkoli narobe se stanje v bazi povrne v prvotno stanje
            with transaction.atomic():
                aktivnost_create_form.instance = aktivnost
                aktivnost_create_form_saved = aktivnost_create_form.save()

                if kontrolni_list_create_formset.is_valid():
                    kontrolni_list_create_formset.instance = aktivnost_create_form_saved
                    kontrolni_list_create_formset.save()

            return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': aktivnost.opravilo.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'aktivnost_create_form': aktivnost_create_form,
                'kontrolni_list_create_formset': kontrolni_list_create_formset,
                },
            )


class KontrolaVrednostCreateView(LoginRequiredMixin, UpdateView):
    model = DelovniNalog
    template_name = 'kontrolnilist/kontrola_vrednost_create.html'
    fields = ('id', )


    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)


        # logika za izdelavo vrednosti specificiranih kontrol

        aktivnost_list = Aktivnost.objects.not_deleted()  # samo status ne izbrisano
        aktivnost_list = aktivnost_list.filter(opravilo=dn.opravilo)  # aktivnost v obstoječem delovnem nalogu
        for aktivnost in aktivnost_list:
            ks_list = KontrolaSpecifikacija.objects.filter(kontrola_skupina__aktivnost=aktivnost)

            for ks in ks_list:
                 projektna_mesta_specifikacije = ks.projektno_mesto.all()
                 for pm in projektna_mesta_specifikacije:
                    kontrola_vrednost = KontrolaVrednost.objects.create(
                            delovni_nalog=dn,
                            kontrola_specifikacija=ks,
                            projektno_mesto=pm,
                        )

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))



    def get_context_data(self, *args, **kwargs):
        context = super(KontrolaVrednostCreateView, self).get_context_data(*args, **kwargs)
        # new context data go here

        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class KontrolniListUpdateOblika01View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/update_oblika01.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListUpdateOblika01View, self).get_context_data(*args, **kwargs)


        dn = DelovniNalog.objects.get(id=self.object.id)

        # Kontrolni List
        kontrola_vrednost_update_formset = KontrolaVrednostUpdateFormSetOblika01(delovninalog=dn)
        context['kontrola_vrednost_update_oblika01_formset'] = kontrola_vrednost_update_formset



        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)
        formset = KontrolaVrednostUpdateFormSetOblika01(request.POST or None, delovninalog=dn)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))
        else:
            return render(
                request,
                self.template_name,
                {
                    'kontrola_vrednost_update_formset': kontrola_vrednost_update_formset,
                },
            )

class KontrolniListUpdateOblika02View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/update_oblika02.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListUpdateOblika02View, self).get_context_data(*args, **kwargs)


        dn = DelovniNalog.objects.get(id=self.object.id)

        # Kontrolni List
        kontrola_vrednost_update_formset = KontrolaVrednostUpdateFormSetOblika02(delovninalog=dn)
        context['kontrola_vrednost_update_oblika02_formset'] = kontrola_vrednost_update_formset



        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)

        formset = KontrolaVrednostUpdateFormSetOblika02(request.POST or None, delovninalog=dn)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))
        else:
            return render(
                request,
                self.template_name,
                {
                    'kontrola_vrednost_update_formset': kontrola_vrednost_update_formset,
                },
            )


class KontrolniListPrintOblika01View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/print_oblika01.html'
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListPrintOblika01View, self).get_context_data(*args, **kwargs)

        dn = DelovniNalog.objects.get(id=self.object.id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):


        dn = DelovniNalog.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")

        vrednost_list = KontrolaVrednost.objects.filter(delovni_nalog=dn)

        # razporeditev
        vrednost_list = vrednost_list.order_by(
            # glede na etažo
            '-projektno_mesto__lokacija__etaza__elevation',
            # glede na prostor
            'projektno_mesto__lokacija__prostor',
            # glede na projektno mesto
            'projektno_mesto',
            # glede na aktivnost
            'kontrola_specifikacija__kontrola_skupina__aktivnost__zap_st',
            'kontrola_specifikacija__kontrola_skupina__aktivnost__oznaka',
            # glede na skupino kontrol
            'kontrola_specifikacija__kontrola_skupina__zap_st',
            'kontrola_specifikacija__kontrola_skupina__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__zap_st',
            'kontrola_specifikacija__oznaka',
            )

        print(vrednost_list)

        # iz instance pridobimo željene podatke
        # ki jih bomo uporabili v izpisu
        vrsta_dokumenta = "KONTROLNI LIST"
        opravilo = dn.opravilo
        narocilo = dn.opravilo.narocilo
        datum = timezone.localtime(timezone.now()).date()

        izpis_data = {
            'vrednost_list': vrednost_list,
            'delovninalog': dn,
            'opravilo': opravilo,
            'narocilo': narocilo,
            'datum': datum,
        }



        # izdelamo izpis
        filename = fill_template(
            # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
            'obrazci/kontrolnilist/kontrolni_list_oblika01_20171216.ods',
            # podatki za uporabo v oblikovni datoteki
            izpis_data,
            output_format="xlsx"
        )

        visible_filename = '{}.{}'.format(dn.oznaka ,"xlsx")

        return FileResponse(filename, visible_filename)


class KontrolniListPrintOblika02View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/print_oblika02.html'
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListPrintOblika02View, self).get_context_data(*args, **kwargs)

        dn = DelovniNalog.objects.get(id=self.object.id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")

        vrednost_list = KontrolaVrednost.objects.filter(delovni_nalog=dn)

        # razporeditev
        vrednost_list = vrednost_list.order_by(
            # glede na aktivnost
            'kontrola_specifikacija__kontrola_skupina__aktivnost__zap_st',
            'kontrola_specifikacija__kontrola_skupina__aktivnost__oznaka',
            # glede na del stavbe
            'projektno_mesto__del_stavbe',
            # glede na projektno mesto
            'projektno_mesto__oznaka',
            # glede na skupino kontrol
            'kontrola_specifikacija__kontrola_skupina__zap_st',
            'kontrola_specifikacija__kontrola_skupina__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__zap_st',
            'kontrola_specifikacija__oznaka',
            )

        # iz instance pridobimo željene podatke
        # ki jih bomo uporabili v izpisu
        vrsta_dokumenta = "KONTROLNI LIST"
        opravilo = dn.opravilo
        narocilo = dn.opravilo.narocilo
        datum = timezone.localtime(timezone.now()).date()

        izpis_data = {
            'vrednost_list': vrednost_list,
            'delovninalog': dn,
            'opravilo': opravilo,
            'narocilo': narocilo,
            'datum': datum,
        }



        # izdelamo izpis
        filename = fill_template(
            # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
            'obrazci/kontrolnilist/kontrolni_list_oblika02_20171216.ods',
            # podatki za uporabo v oblikovni datoteki
            izpis_data,
            output_format="xlsx"
        )

        visible_filename = '{}.{}'.format(dn.oznaka ,"xlsx")

        return FileResponse(filename, visible_filename)




class OpraviloKontrolniListCreateView(LoginRequiredMixin, UpdateView):
    '''
    Izdelava kontrolnega lista za nazaj. Če ima opravilo definirano planirano_opravilo
    se izdela kontrolni list glede na izbrano planirano opravilo  . Če obstaja
    '''
    model = Opravilo
    template_name = "kontrolnilist/create_from_opravilo.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloKontrolniListCreateView, self).get_context_data(*args, **kwargs)

        return context

    def post(self, request, *args, **kwargs):

        # object
        opravilo = Opravilo.objects.get(id=self.get_object().id)


        if opravilo.planirano_opravilo:

            planirano_opravilo = opravilo.planirano_opravilo

            # izdelati moramo aktivnost in pripadajoče specifikacije kontrol
            plan_aktivnost_list = planirano_opravilo.planaktivnost_set.all()

            for pa in plan_aktivnost_list:
                # dodamo aktivnosti
                aktivnost = Aktivnost.objects.create(
                    oznaka=pa.oznaka,
                    naziv=pa.naziv,
                    opis=pa.opis,
                    perioda_enota=pa.perioda_enota,
                    perioda_enota_kolicina=pa.perioda_enota_kolicina,
                    perioda_kolicina_na_enoto=pa.perioda_kolicina_na_enoto,
                    zap_st=pa.zap_st,
                    status=pa.status,
                    plan_aktivnost=pa,
                    opravilo=opravilo,

                )
                aktivnost.save()


                # izdelamo skupine kontrol če obstajajo
                if pa.plankontrolaskupina_set:
                    pksk_list = pa.plankontrolaskupina_set.all()
                    for pksk in pksk_list:
                        kontrola_skupina = KontrolaSkupina.objects.create(
                            oznaka=pksk.oznaka,
                            naziv=pksk.naziv,
                            plan_kontrola_skupina=pksk,  # pomembno zaradi navezave
                            zap_st=pksk.zap_st,
                            status=pksk.status,
                            aktivnost=aktivnost,

                        )

                        kontrola_skupina.save()

                        # dodamo še specifikacijo kontrol
                        plan_kontrola_specifikacija_list = pksk.plankontrolaspecifikacija_set.all()
                        for pks in plan_kontrola_specifikacija_list:

                            kontrola_specifikacija = KontrolaSpecifikacija.objects.create(
                                oznaka=pks.oznaka,
                                naziv=pks.naziv,
                                opis=pks.opis,
                                vrednost_vrsta=pks.vrednost_vrsta,
                                zap_st=pks.zap_st,
                                status=pks.status,
                                plan_kontrola_specifikacija=pks,
                                kontrola_skupina=kontrola_skupina,
                            )

                            kontrola_specifikacija.save()
                            # dodamo še projektna mesta
                            kontrola_specifikacija.projektno_mesto = pks.projektno_mesto.all()
                            kontrola_specifikacija.save()

                            # če je vrsta SELECT (=3) dodamo še opcije select
                            if pks.vrednost_vrsta == 3:
                                pos_list = pks.plankontrolaspecifikacijaopcijaselect_set.all()
                                for pos in pos_list:
                                    kontrola_specifikacija_opcija_select = KontrolaSpecifikacijaOpcijaSelect.objects.create(
                                        oznaka=pos.oznaka,
                                        naziv=pos.naziv,
                                        opis=pos.opis,
                                        kontrola_specifikacija=kontrola_specifikacija,
                                    )


            return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk}))

        else:
            return render(request, self.template_name, {

                }
            )
