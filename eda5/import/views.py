import csv
import io
import os

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from .forms import UvozCsvForm

from eda5.partnerji.forms import PostaCreateForm, PartnerCreateForm
from eda5.partnerji.models import Posta

from eda5.deli.forms import SkupinaCreateForm, PodskupinaCreateForm
from eda5.deli.models import Skupina

from eda5.racunovodstvo.forms import KontoCreateForm, PodkontoCreateForm, SkupinaVrsteStroskaCreateForm,\
                                     VrstaStroskaCreateForm
from eda5.racunovodstvo.models import Konto, PodKonto, SkupinaVrsteStroska

from eda5.delovninalogi.forms import DeloVrstaSklopCreateForm, DeloVrstaCreateForm
from eda5.delovninalogi.models import DeloVrstaSklop


class UvozCsv(TemplateView):
    template_name = "import/form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UvozCsv, self).get_context_data(*args, **kwargs)
        context['uvoz_form'] = UvozCsvForm
        return context

    def post(self, request, *args, **kwargs):
        uvoz_form = UvozCsvForm(request.POST or None)

        def import_poste():
            filename = os.path.abspath("eda5/templates/import/partnerji/poste_slovenije.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form1 = PostaCreateForm(row)
                if form1.is_valid():
                    form1.save()
                    records_added += 1

            return messages.success(request, "Število dodanih vnosov pošte: %s" % (records_added))

        def import_partnerji():

            filename = os.path.abspath("eda5/templates/import/partnerji/partnerji_edafm.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                print(row)
                postna_stevilka = row['posta']
                print(postna_stevilka)
                try:
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)
                except:
                    # print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    # posta = Posta.objects.get(postna_stevilka=5000)  # uvozimo pod nepravo poštno številko
                    # ODVISNOSTI
                    import_poste()

                row['posta'] = posta.pk
                form2 = PartnerCreateForm(row)

                if form2.is_valid():
                    form2.save()
                    records_added += 1

            return messages.success(request, "Število novo dodanih parnerjev: %s" % (records_added))

        def import_deli_skupine():

            filename = os.path.abspath("eda5/templates/import/deli/skupine.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = SkupinaCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "SKUPINE DELOV STAVBE: Število dodanih vnosov: %s" % (records_added))

        def import_deli_podskupine():

            filename = os.path.abspath("eda5/templates/import/deli/podskupine.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                skupina_oznaka = row['skupina']
                try:
                    skupina = Skupina.objects.get(oznaka=skupina_oznaka)
                except:
                    import_deli_skupine()

                row['skupina'] = skupina.pk
                form = PodskupinaCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "DELI:PODSKUPINE Število dodanih vnosov: %s" % (records_added))

        def import_racunovodstvo_konto():

            filename = os.path.abspath("eda5/templates/import/racunovodstvo/konto.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = KontoCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "RACUNOVODSTVO:KONTO Število dodanih vnosov: %s" % (records_added))

        def import_racunovodstvo_podkonto():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/racunovodstvo/podkonto.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            for row in seznam:

                # oznako skupine zamenjamo z ID skupine
                konto_oznaka = row['skupina']
                try:
                    konto = Konto.objects.get(oznaka=konto_oznaka)
                    row['skupina'] = konto.pk
                    form = PodkontoCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_racunovodstvo_konto()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "RACUNOVODSTVO:PODKONTO Število dodanih vnosov: %s" % (records_added))

        def import_racunovodstvo_skupina_vrst_stroskov():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/racunovodstvo/skupina_vrste_stroska.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            for row in seznam:

                # oznako skupine zamenjamo z ID skupine
                podkonto_oznaka = row['skupina']
                try:
                    podkonto = PodKonto.objects.get(oznaka=podkonto_oznaka)
                    row['skupina'] = podkonto.pk
                    form = SkupinaVrsteStroskaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_racunovodstvo_podkonto()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(
                request,
                "RACUNOVODSTVO:SKUPINA_VRSTE_STROSKA Število dodanih vnosov: %s" % (records_added)
            )

        def import_racunovodstvo_vrste_stroskov():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/racunovodstvo/vrsta_stroska.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            for row in seznam:

                # oznako skupine zamenjamo z ID skupine
                skupina_vrste_stroska_oznaka = row['skupina']
                try:
                    skupina_vrste_stroska = SkupinaVrsteStroska.objects.get(oznaka=skupina_vrste_stroska_oznaka)
                    row['skupina'] = skupina_vrste_stroska.pk
                    form = VrstaStroskaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_racunovodstvo_skupina_vrst_stroskov()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "RACUNOVODSTVO:VRSTA_STROSKA Število dodanih vnosov: %s" % (records_added))

        def import_delovninalog_delo_vrsta_sklop():

            filename = os.path.abspath("eda5/templates/import/delovninalogi/delo_vrsta_sklop.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = DeloVrstaSklopCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "DELOVNI_NALOGI:DELO_VRSTA_SKLOP Število dodanih vnosov: %s" % (records_added))

        def import_delovninalog_delo_vrsta():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/delovninalogi/delo_vrsta.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            for row in seznam:

                # oznako skupine zamenjamo z ID skupine
                delo_vrsta_sklop_oznaka = row['skupina']
                try:
                    delo_vrsta_sklop = DeloVrstaSklop.objects.get(oznaka=delo_vrsta_sklop_oznaka)
                    row['skupina'] = delo_vrsta_sklop.pk
                    form = DeloVrstaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_delovninalog_delo_vrsta_sklop()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "DELOVNI_NALOGI:DELO_VRSTA Število dodanih vnosov: %s" % (records_added))

        if uvoz_form.is_valid():

            if uvoz_form.cleaned_data['poste'] is True:
                import_poste()

            if uvoz_form.cleaned_data['partnerji'] is True:
                import_partnerji()

            if uvoz_form.cleaned_data['skupine_delov_stavbe'] is True:
                import_deli_podskupine()

            if uvoz_form.cleaned_data['stroskovna_mesta'] is True:
                import_racunovodstvo_vrste_stroskov()

            if uvoz_form.cleaned_data['vrste_del'] is True:
                import_delovninalog_delo_vrsta()

        return HttpResponseRedirect(reverse('moduli:import:form'))
