# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.db.models import Value
from django.db.models.functions import Concat

# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import DelovniNalog
from eda5.deli.models import DelStavbe, ProjektnoMesto
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek, PodKonto, SkupinaVrsteStroska, VrstaStroska


# Forms
from ..forms import \
    FormatForm,\
    LetnoPorociloUpravnikaStroskiIzpisIzbiraForm,\
    PlanIzbiraForm, LetoIzbiraForm,\
    IzvedenaDelaIzpisIzbiraForm,\
    UporabimFilterForm,\
    ObracunIzrednaDelaForm,\
    DogodekFilterForm,\
    DogodkiIzpisIzbiraForm


# Views
from eda5.core.views import FilteredListView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse


class PorocanjeStroskiView(LoginRequiredMixin, TemplateView):
    template_name = "reports/letno_porocilo_upravnika/porocanje_stroski.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeStroskiView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_STROSKI")
        context['modul_zavihek'] = modul_zavihek

        letno_porocilo_upravnika_izpis_izbira_form = LetnoPorociloUpravnikaStroskiIzpisIzbiraForm()
        context['letno_porocilo_upravnika_izpis_izbira_form'] = letno_porocilo_upravnika_izpis_izbira_form

        # seznam stroškov

        return context


    def get(self, request, *args, **kwargs):

        # osnovni seznam, ki ga bomo filtrirali
        strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1).order_by('datum_storitve_od')
        strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka')
        strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_mesec__oznaka')


        # Forms za Filtriranje

        # Na začetku so vsi neustrezni

        # Pridobimo podatke iz formsu


        # Izdelamo filtriran seznam glede
        # v specifičnem letu
        strosek_list = strosek_list.filter(strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka="2017")


        # Izpišemo podatke v context

        context = self.get_context_data(
            strosek_list=strosek_list,
        )

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_STROSKI")

        format_form = FormatForm(request.POST or None)
        format_form_is_valid = True

        letno_porocilo_upravnika_izpis_izbira_form = LetnoPorociloUpravnikaStroskiIzpisIzbiraForm(request.POST or None)
        letno_porocilo_upravnika_izpis_izbira_form_is_valid = False

        if letno_porocilo_upravnika_izpis_izbira_form.is_valid():

            izpis_izbira = letno_porocilo_upravnika_izpis_izbira_form.cleaned_data['izpis_izbira']
            letno_porocilo_upravnika_izpis_izbira_form_is_valid = True

        if format_form_is_valid == True:

            strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1).order_by('datum_storitve_od')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_mesec__oznaka')

            strosek_list = strosek_list.exclude(vrsta_stroska__skupina__skupina__oznaka="ONU")

            strosek_list = strosek_list.filter(strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka="2017")


            if letno_porocilo_upravnika_izpis_izbira_form_is_valid == True:

                if izpis_izbira == '1':

                    self.strosek_list = strosek_list

                    izpis_data = {
                        'strosek_list': strosek_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_stroski.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_stroski' ,"xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '2':


                    strosek_skupina_list = PodKonto.objects.filter(skupinavrstestroska__vrstastroska__strosek__in=strosek_list)
                    strosek_skupina_list = strosek_skupina_list.distinct()
                    strosek_skupina_list = strosek_skupina_list.annotate(znesek_brez_ddv=Sum('skupinavrstestroska__vrstastroska__strosek__osnova'))
                    strosek_skupina_list = strosek_skupina_list.order_by('skupina__zap_st', 'zap_st')

                    self.strosek_skupina_list = strosek_skupina_list


                    izpis_data = {
                        'strosek_skupina_list': strosek_skupina_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_strosek_skupina_list.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_strosek_skupina_list' ,"xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '3':


                    strosek_vrsta_list = VrstaStroska.objects.filter(strosek__in=strosek_list)
                    strosek_vrsta_list = strosek_vrsta_list.distinct()
                    strosek_vrsta_list = strosek_vrsta_list.annotate(znesek_brez_ddv=Sum('strosek__osnova'))
                    strosek_vrsta_list = strosek_vrsta_list.order_by('skupina__skupina__skupina__zap_st', 'skupina__skupina__zap_st', 'skupina__zap_st', 'zap_st')

                    self.strosek_vrsta_list = strosek_vrsta_list


                    izpis_data = {
                        'strosek_vrsta_list': strosek_vrsta_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_strosek_vrsta_list.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_strosek_vrsta_list' ,"xlsx")

                    return FileResponse(filename, visible_filename)


        # IF NOT VALID
        return render(
            request, self.template_name, {
                'format_form': format_form,
                'letno_porocilo_upravnika_izpis_izbira_form': letno_porocilo_upravnika_izpis_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class PorocanjeIzvedenaDelaView(LoginRequiredMixin, TemplateView):
    template_name = "reports/letno_porocilo_upravnika/porocanje_izvedena_dela.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeIzvedenaDelaView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_IZVEDENA_DELA")
        context['modul_zavihek'] = modul_zavihek

        izpis_izbira_form = IzvedenaDelaIzpisIzbiraForm()
        context['izpis_izbira_form'] = izpis_izbira_form

        izredna_dela_filter_form = ObracunIzrednaDelaForm()
        context['izredna_dela_filter_form'] = izredna_dela_filter_form




        # seznam stroškov

        return context


    def get(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_IZVEDENA_DELA")


        # form za filtriranje
        uporabim_filter_form = UporabimFilterForm(request.GET or None)
        plan_izbira_form = PlanIzbiraForm(request.GET or None)
        leto_izbira_form = LetoIzbiraForm(request.GET or None)

        # na začetku so vsi formi neustrezni
        uporabim_filter_form_is_valid = False
        plan_izbira_form_is_valid = False
        leto_izbira_form_is_valid = False

        # osnovni seznam, ki ga bomo filtrirali

        if uporabim_filter_form.is_valid():
            # izpis_izbira = izpis_izbira_form.cleaned_data['izpis_izbira']
            uporabim_filter_form_is_valid = True


        if uporabim_filter_form_is_valid == True:
            dn_list = DelovniNalog.objects.filter()
            dn_list = dn_list.order_by('opravilo__planirano_opravilo__osnova__zap_st', 'opravilo__planirano_opravilo__oznaka', 'datum_stop')

            dn_list = dn_list.annotate(planirano_opravilo_osnova = Concat('opravilo__planirano_opravilo__osnova__oznaka', Value(' - '), 'opravilo__planirano_opravilo__osnova__naziv'))
            dn_list = dn_list.annotate(planirano_opravilo = Concat('opravilo__planirano_opravilo__oznaka', Value(' - '), 'opravilo__planirano_opravilo__naziv'))


            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                leto_izbira_form_is_valid = True

            if plan_izbira_form.is_valid():
                izbrani_plan = plan_izbira_form.cleaned_data['izbrani_plan']
                plan_izbira_form_is_valid = True



            if leto_izbira_form_is_valid == True:
                dn_list = dn_list.filter(datum_stop__year=obdobje_leto.oznaka)

            if plan_izbira_form_is_valid == True:
                dn_list = dn_list.filter(opravilo__planirano_opravilo__plan=izbrani_plan)

        else:

            dn_list = []



        context = self.get_context_data(
            uporabim_filter_form=uporabim_filter_form,
            plan_izbira_form=plan_izbira_form,
            leto_izbira_form=leto_izbira_form,
            dn_list=dn_list,
            modul_zavihek=modul_zavihek,
        )

        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_IZVEDENA_DELA")




        # form za filtriranje
        format_form = FormatForm(request.POST or None)
        izpis_izbira_form = IzvedenaDelaIzpisIzbiraForm(request.POST or None)
        plan_izbira_form = PlanIzbiraForm(request.POST or None)
        leto_izbira_form = LetoIzbiraForm(request.POST or None)
        izredna_dela_filter_form = ObracunIzrednaDelaForm(request.POST or None)

        # na začetku so vsi formi neustrezni
        izpis_izbira_form_is_valid = False
        plan_izbira_form_is_valid = False
        leto_izbira_form_is_valid = False
        format_form_is_valid = True
        izredna_dela_filter_form_is_valid = False

        # osnovni seznam, ki ga bomo filtrirali

        if izpis_izbira_form.is_valid():
            izpis_izbira = izpis_izbira_form.cleaned_data['izpis_izbira']
            izpis_izbira_form_is_valid = True



        if format_form_is_valid == True:


            dn_list = DelovniNalog.objects.filter()
            dn_list = dn_list.order_by('opravilo__planirano_opravilo__osnova__zap_st', 'opravilo__planirano_opravilo__oznaka', 'datum_stop')

            dn_izredno_list = dn_list.filter(opravilo__planirano_opravilo__isnull=True)


            if izpis_izbira_form_is_valid == True:

                if izpis_izbira == '1':
                    dn_list = dn_list.annotate(planirano_opravilo_osnova = Concat('opravilo__planirano_opravilo__osnova__oznaka', Value(' - '), 'opravilo__planirano_opravilo__osnova__naziv'))
                    dn_list = dn_list.annotate(planirano_opravilo = Concat('opravilo__planirano_opravilo__oznaka', Value(' - '), 'opravilo__planirano_opravilo__naziv'))



                    if leto_izbira_form.is_valid():
                        obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                        leto_izbira_form_is_valid = True

                    if plan_izbira_form.is_valid():
                        izbrani_plan = plan_izbira_form.cleaned_data['izbrani_plan']
                        plan_izbira_form_is_valid = True



                    if leto_izbira_form_is_valid == True:
                        dn_list = dn_list.filter(datum_stop__year=obdobje_leto.oznaka)

                    if plan_izbira_form_is_valid == True:
                        dn_list = dn_list.filter(opravilo__planirano_opravilo__plan=izbrani_plan)


                    izpis_data = {
                        'plan_oznaka': izbrani_plan.oznaka,
                        'plan_naziv': izbrani_plan.naziv,
                        'obdobje_leto': obdobje_leto,
                        'dn_list': dn_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_izvedena_dela.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{} {}-{}.{}'.format('Izvedena planirana opravila', izbrani_plan.oznaka, obdobje_leto, "xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '2':

                    if izredna_dela_filter_form.is_valid():
                        vrsta_stroska = izredna_dela_filter_form.cleaned_data['vrsta_stroska']
                        narocilo = izredna_dela_filter_form.cleaned_data['narocilo']
                        datum_od = izredna_dela_filter_form.cleaned_data['datum_od']
                        datum_do = izredna_dela_filter_form.cleaned_data['datum_do']
                        izredna_dela_filter_form_is_valid = True

                    if izredna_dela_filter_form_is_valid == True:
                        dn_izredno_list = dn_izredno_list.filter(opravilo__vrsta_stroska=vrsta_stroska)
                        dn_izredno_list = dn_izredno_list.filter(opravilo__narocilo=narocilo)
                        dn_izredno_list = dn_izredno_list.filter(datum_start__gte=datum_od)
                        dn_izredno_list = dn_izredno_list.filter(datum_start__lte=datum_do)
                        dn_izredno_list = dn_izredno_list.order_by('datum_start')


                    izpis_data = {
                        'vrsta_stroska_oznaka': vrsta_stroska.oznaka,
                        'vrsta_stroska_naziv': vrsta_stroska.naziv,
                        'obdobje_od': datum_od,
                        'obdobje_do': datum_do,
                        'obdobje_leto': datum_od.year,
                        'dn_list': dn_izredno_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_izvedena_dela_izredna.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{} {}-{}.{}'.format('Izvedena izredna dela', vrsta_stroska.oznaka, datum_od.year, "xlsx")

                    return FileResponse(filename, visible_filename)


                if izpis_izbira == '3':

                    if izredna_dela_filter_form.is_valid():
                        vrsta_stroska = izredna_dela_filter_form.cleaned_data['vrsta_stroska']
                        datum_od = izredna_dela_filter_form.cleaned_data['datum_od']
                        datum_do = izredna_dela_filter_form.cleaned_data['datum_do']
                        izredna_dela_filter_form_is_valid = True

                    if izredna_dela_filter_form_is_valid == True:
                        dn_izredno_list = dn_izredno_list.filter(opravilo__vrsta_stroska=vrsta_stroska)
                        dn_izredno_list = dn_izredno_list.filter(datum_start__gte=datum_od)
                        dn_izredno_list = dn_izredno_list.filter(datum_start__lte=datum_do)

                        del_list = DelStavbe.objects.filter()
                        # del_list = del_list.exclude(podskupina__oznaka="CA")

                        projektno_mesto_list = ProjektnoMesto.objects.filter()
                        projektno_mesto_list = projektno_mesto_list.filter(del_stavbe__in=del_list)

                        dn_izredno_list = dn_izredno_list.filter(opravilo__element__in=projektno_mesto_list)
                        dn_izredno_list = dn_izredno_list.distinct()

                        dn_izredno_list = dn_izredno_list.order_by('datum_start')


                    izpis_data = {
                        'vrsta_stroska_oznaka': vrsta_stroska.oznaka,
                        'vrsta_stroska_naziv': vrsta_stroska.naziv,
                        'obdobje_od': datum_od,
                        'obdobje_do': datum_do,
                        'obdobje_leto': datum_od.year,
                        'dn_list': dn_izredno_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_izvedena_dela_izredna.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{} {}-{}.{}'.format('Izvedena izredna dela', vrsta_stroska.oznaka, datum_od.year, "xlsx")

                    return FileResponse(filename, visible_filename)



        # IF NOT VALID
        return render(
            request, self.template_name, {
                'format_form': format_form,
                'izpis_izbira_form': izpis_izbira_form,
                'plan_izbira_form': plan_izbira_form,
                'leto_izbira_form': leto_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class PorocanjeDogodkiView(LoginRequiredMixin, TemplateView):
    template_name = "reports/letno_porocilo_upravnika/porocanje_dogodki.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeDogodkiView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_DOGODKI")
        context['modul_zavihek'] = modul_zavihek

        izpis_izbira_form = DogodkiIzpisIzbiraForm()
        context['izpis_izbira_form'] = izpis_izbira_form



        return context


    def get(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_DOGODKI")

        # form za filtriranje
        uporabim_filter_form = UporabimFilterForm(request.GET or None)
        leto_izbira_form = LetoIzbiraForm(request.GET or None)
        dogodek_filter_form =  DogodekFilterForm(request.GET or None)

        # na začetku so vsi formi neustrezni
        uporabim_filter_form_is_valid = False
        leto_izbira_form_is_valid = False
        dogodek_filter_form_is_valid = False

        # osnovni seznam, ki ga bomo filtrirali

        if uporabim_filter_form.is_valid():
            # izpis_izbira = izpis_izbira_form.cleaned_data['izpis_izbira']
            uporabim_filter_form_is_valid = True


        if uporabim_filter_form_is_valid == True:
            dogodek_list = Dogodek.objects.filter()
            dogodek_list = dogodek_list.order_by('datum_dogodka', 'cas_dogodka')


            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                leto_izbira_form_is_valid = True

            if leto_izbira_form_is_valid == True:
                dogodek_list = dogodek_list.filter(datum_dogodka__year=obdobje_leto.oznaka)


            if dogodek_filter_form.is_valid():
                zavarovani_dogodki = dogodek_filter_form.cleaned_data['zavarovani_dogodki']
                nezavarovani_dogodki = dogodek_filter_form.cleaned_data['nezavarovani_dogodki']
                dogodek_filter_form_is_valid = True

            if dogodek_filter_form_is_valid == True:
                if zavarovani_dogodki == True:
                    dogodek_list = dogodek_list.filter(prijava_skode__isnull=False)

                if nezavarovani_dogodki == True:
                    dogodek_list = dogodek_list.filter(prijava_skode__isnull=True)

        else:

            dogodek_list = []


        context = self.get_context_data(
            uporabim_filter_form=uporabim_filter_form,
            leto_izbira_form=leto_izbira_form,
            dogodek_filter_form=dogodek_filter_form,
            dogodek_list=dogodek_list,
            modul_zavihek=modul_zavihek,
        )

        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_DOGODKI")

        # form za filtriranje
        format_form = FormatForm(request.POST or None)
        uporabim_filter_form = UporabimFilterForm(request.POST or None)
        leto_izbira_form = LetoIzbiraForm(request.POST or None)
        dogodek_filter_form =  DogodekFilterForm(request.POST or None)
        izpis_izbira_form = DogodkiIzpisIzbiraForm(request.POST or None)

        # na začetku so vsi formi neustrezni
        uporabim_filter_form_is_valid = False
        leto_izbira_form_is_valid = False
        dogodek_filter_form_is_valid = False
        izpis_izbira_form_is_valid = False
        format_form_is_valid = True

        # form za filtriranje

        # osnovni seznam, ki ga bomo filtrirali

        if izpis_izbira_form.is_valid():
            izpis_izbira = izpis_izbira_form.cleaned_data['izpis_izbira']
            izpis_izbira_form_is_valid = True



        if format_form_is_valid == True:

            dogodek_list = Dogodek.objects.filter()
            dogodek_list = dogodek_list.order_by('datum_dogodka', 'cas_dogodka')

            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                leto_izbira_form_is_valid = True

            if leto_izbira_form_is_valid == True:
                dogodek_list = dogodek_list.filter(datum_dogodka__year=obdobje_leto.oznaka)


            if dogodek_filter_form.is_valid():
                zavarovani_dogodki = dogodek_filter_form.cleaned_data['zavarovani_dogodki']
                nezavarovani_dogodki = dogodek_filter_form.cleaned_data['nezavarovani_dogodki']
                dogodek_filter_form_is_valid = True

            if dogodek_filter_form_is_valid == True:
                if zavarovani_dogodki == True:
                    dogodek_list = dogodek_list.filter(prijava_skode__isnull=False)

                if nezavarovani_dogodki == True:
                    dogodek_list = dogodek_list.filter(prijava_skode__isnull=True)



            if izpis_izbira_form_is_valid == True:

                if izpis_izbira == '1':
                    dogodek_list = dogodek_list.filter(prijava_skode__isnull=False)

                    izpis_data = {
                        'obdobje_leto': obdobje_leto,
                        'dogodek_list': dogodek_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_zavarovane_skode.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{} {}.{}'.format('Škode krite iz naslova pogodb z zavarovalnico', obdobje_leto, "xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '2':


                    izpis_data = {
                        'obdobje_leto': obdobje_leto,
                        'dogodek_list': dogodek_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_dogodki.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{} {}.{}'.format('Pomembni dogodki v letu', obdobje_leto, "xlsx")

                    return FileResponse(filename, visible_filename)




        # IF NOT VALID
        return render(
            request, self.template_name, {
                'format_form': format_form,
                'izpis_izbira_form': izpis_izbira_form,
                'plan_izbira_form': plan_izbira_form,
                'leto_izbira_form': leto_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )
