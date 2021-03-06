import csv
import io
import os

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from .forms import UtilitiUvozCsvForm, PartnerjiUvozCsvForm, DeliUvozCsvForm, RacunovodstvoUvozCsvForm,\
                   DelovniNalogiUvozCsvForm, EtaznaLastninaUvozCsvForm, KatalogUvozCsvForm, PostaUvozCsvForm,\
                   PredpisiUvozCsvForm, StevcnoStanjeUvozCsvForm, ModuliUvozCsvForm

from eda5.core.forms import ObdobjeLetoCreateForm, ObdobjeMesecCreateForm

from eda5.partnerji.forms import PostaCreateForm, PartnerCreateForm, BankaCreateForm, DrzavaCreateForm
from eda5.partnerji.models import Partner, Posta, Drzava, SkupinaPartnerjev

# Deli FORMS
from eda5.deli.forms import \
    skupina_forms, \
    podskupina_forms

# Deli MODELS
from eda5.deli.models import \
    Skupina

from eda5.racunovodstvo.forms.racun_forms import KontoCreateForm, PodkontoCreateForm
from eda5.racunovodstvo.forms.vrsta_stroska_forms import SkupinaVrsteStroskaCreateForm, VrstaStroskaCreateForm
from eda5.racunovodstvo.models import Konto, PodKonto, SkupinaVrsteStroska

from eda5.delovninalogi.forms import DeloVrstaSklopCreateForm, DeloVrstaCreateForm
from eda5.delovninalogi.models import DeloVrstaSklop

from eda5.etaznalastnina.forms import ProgramCreateForm, LastniskaEnotaElaboratCreateForm,\
                                      LastniskaEnotaInternaCreateForm, LastniskaSkupinaCreateForm,\
                                      UporabnoDovoljenjeCreateForm, InternaDodatnoCreateForm
from eda5.etaznalastnina.models import Program, LastniskaEnotaElaborat, LastniskaEnotaInterna, UporabnoDovoljenje

from eda5.katalog.forms import TipArtiklaCreateForm, ProizvajalecCreateForm, ModelArtiklaCreateForm
from eda5.katalog.models import Proizvajalec ,TipArtikla

from eda5.posta.forms import SkupinaDokumentaCreateForm, VrstaDokumentaCreateForm
from eda5.posta.models import SkupinaDokumenta

# Predpisi
from eda5.predpisi.forms import PredpisSklopCreateForm, PredpisPodsklopCreateForm
from eda5.predpisi.forms import PredpisOpraviloCreateForm, PredpisCreateForm
from eda5.predpisi.models import PredpisSklop, PredpisPodsklop, PredpisOpravilo, Predpis

# StevcnoStanje
from eda5.stevcnostanje.forms import StevecCreateForm, StevecStatusCreateForm, DelilnikCreateForm, OdcitekCreateForm
from eda5.stevcnostanje.models import Stevec, Delilnik, StevecStatus, Odcitek

from eda5.users.forms import UserCreateForm

# Moduli
from eda5.moduli.forms import ModulCreateForm, ZavihekCreateForm
from eda5.moduli.models import Modul, Zavihek


class UvozCsv(TemplateView):
    template_name = "import/form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UvozCsv, self).get_context_data(*args, **kwargs)

        # forms
        context['utiliti_uvoz_form'] = UtilitiUvozCsvForm
        context['partnerji_uvoz_form'] = PartnerjiUvozCsvForm
        context['deli_uvoz_form'] = DeliUvozCsvForm
        context['racunovodstvo_uvoz_form'] = RacunovodstvoUvozCsvForm
        context['delovninalogi_uvoz_form'] = DelovniNalogiUvozCsvForm
        context['etaznalastnina_uvoz_form'] = EtaznaLastninaUvozCsvForm
        context['katalog_uvoz_form'] = KatalogUvozCsvForm
        context['posta_uvoz_form'] = PostaUvozCsvForm
        context['predpisi_uvoz_form'] = PredpisiUvozCsvForm
        context['stevcno_stanje_uvoz_form'] = StevcnoStanjeUvozCsvForm
        context['moduli_uvoz_form'] = ModuliUvozCsvForm

        return context

    def post(self, request, *args, **kwargs):
        utiliti_uvoz_form = UtilitiUvozCsvForm(request.POST or None)
        partnerji_uvoz_form = PartnerjiUvozCsvForm(request.POST or None)
        deli_uvoz_form = DeliUvozCsvForm(request.POST or None)
        racunovodstvo_uvoz_form = RacunovodstvoUvozCsvForm(request.POST or None)
        delovninalogi_uvoz_form = DelovniNalogiUvozCsvForm(request.POST or None)
        etaznalastnina_uvoz_form = EtaznaLastninaUvozCsvForm(request.POST or None)
        katalog_uvoz_form = KatalogUvozCsvForm(request.POST or None)
        posta_uvoz_form = PostaUvozCsvForm(request.POST or None)
        predpisi_uvoz_form = PredpisiUvozCsvForm(request.POST or None)
        stevcnostanje_uvoz_form = StevcnoStanjeUvozCsvForm(request.POST or None)
        moduli_uvoz_form = ModuliUvozCsvForm(request.POST or None)

        def import_core_obdobje_leto():

            filename = os.path.abspath("eda5/templates/import/utility/obdobje_leto.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = ObdobjeLetoCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(
                request,
                "DELOVNI_NALOGI:DODANA LETA Število dodanih vnosov: %s" % (records_added)
            )

        def import_core_obdobje_mesec():

            filename = os.path.abspath("eda5/templates/import/utility/obdobje_mesec.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = ObdobjeMesecCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(
                request,
                "DELOVNI_NALOGI:DODANI MESECI Število dodanih vnosov: %s" % (records_added)
            )

        def import_users_admin():

            filename = os.path.abspath("eda5/templates/import/users/admin.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = UserCreateForm(row)

                if form.is_valid():
                    form.save()

            return messages.success(
                request,
                "UTILS: Administratorski uporabnik je dodan"
            )

        def import_utility():
            import_core_obdobje_leto()
            import_core_obdobje_mesec()
            import_users_admin()

        def import_drzava():
            filename = os.path.abspath("eda5/templates/import/partnerji/drzava.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = DrzavaCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "DRŽAVE: Število dodanih vnosov: %s" % (records_added))

        ###############################################################################################################
        # moduli ####################################################################################################
        ###############################################################################################################

        # Modul
        def import_moduli():

            filename = os.path.abspath("eda5/templates/import/moduli/moduli.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = ModulCreateForm(row)
                if form.is_valid():
                    print(row, "--> valid")
                    form.save()
                    records_added += 1
                else:
                    print(row, "--> invalid")

            return messages.success(request, "MODULI / MODUL: Število dodanih vnosov: %s" % (records_added))

        def import_moduli_zavihki():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/moduli/zavihki.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # oznako skupine zamenjamo z ID skupine
                    modul_oznaka = row['modul']
                    modul = Modul.objects.get(oznaka=modul_oznaka)
                    row['modul'] = modul.pk
                    form = ZavihekCreateForm(row)
                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "ZAVIHKI: Število dodanih vnosov: %s" % (records_added))

            except:
                import_moduli()

        def import_poste():
            filename = os.path.abspath("eda5/templates/import/partnerji/poste_slovenije.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                drzava_oznaka = row['drzava']
                try:
                    drzava = Drzava.objects.get(iso_koda=drzava_oznaka)
                    row['drzava'] = drzava.pk
                    form = PostaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    # print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    # posta = Posta.objects.get(postna_stevilka=5000)  # uvozimo pod nepravo poštno številko
                    # ODVISNOSTI
                    import_drzava()

            return messages.success(request, "POSTA: Število dodanih vnosov: %s" % (records_added))

        def import_poste_tujina():
            filename = os.path.abspath("eda5/templates/import/partnerji/poste_tujina.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                drzava_oznaka = row['drzava']
                try:
                    drzava = Drzava.objects.get(iso_koda=drzava_oznaka)
                    row['drzava'] = drzava.pk
                    form = PostaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    # print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    # posta = Posta.objects.get(postna_stevilka=5000)  # uvozimo pod nepravo poštno številko
                    # ODVISNOSTI
                    import_drzava()

            return messages.success(request, "POSTA_TUJINA: Število dodanih vnosov: %s" % (records_added))

        def import_partnerji():

            filename = os.path.abspath("eda5/templates/import/partnerji/partnerji_edafm.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                postna_stevilka = row['posta']
                try:
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)
                    row['posta'] = posta.pk
                    form = PartnerCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    # print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    # posta = Posta.objects.get(postna_stevilka=5000)  # uvozimo pod nepravo poštno številko
                    # ODVISNOSTI
                    import_poste()

            return messages.success(request, "Število novo dodanih parnerjev: %s" % (records_added))

        def partnerji_edafm_update():

            filename = os.path.abspath("eda5/templates/import/partnerji/partnerji_edafm.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:

                postna_stevilka = row['posta']
                posta = Posta.objects.get(postna_stevilka=postna_stevilka)

                # update
                davcna_st = row['davcna_st']
                partner = Partner.objects.get(davcna_st=davcna_st)
                partner.dolgo_ime = row['dolgo_ime']
                partner.kratko_ime = row['kratko_ime']
                partner.naslov = row['naslov']
                partner.posta = posta
                partner.save()

            return messages.success(request, "Partnerji : Update : Končano")

        def import_partnerji_edacenter():

            filename = os.path.abspath("eda5/templates/import/partnerji/partnerji_edacenter.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                postna_stevilka = row['posta']
                try:
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)
                    row['posta'] = posta.pk
                    form = PartnerCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    # print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    # posta = Posta.objects.get(postna_stevilka=5000)  # uvozimo pod nepravo poštno številko
                    # ODVISNOSTI
                    import_poste()
                    import_poste_tujina()

            return messages.success(request, "PARTNER EDA CENTER : Število novo dodanih vnosov: %s" % (records_added))

        def import_partnerji_samo_banke():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/partnerji/partner_banka.csv")
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
                postna_stevilka = row['posta']
                try:
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)
                    row['posta'] = posta.pk
                    form = PartnerCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_poste()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "BANKE: Število dodanih vnosov: %s" % (records_added))

        def import_partnerji_banka():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/partnerji/banka.csv")
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
                partner_davcna_st = row['partner']
                try:
                    partner = Partner.objects.get(davcna_st=partner_davcna_st)
                    row['partner'] = partner.pk
                    form = BankaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_partnerji_samo_banke()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "BANKA-BIC: Število dodanih vnosov: %s" % (records_added))

        def import_deli_skupine():

            filename = os.path.abspath("eda5/templates/import/deli/skupine.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = skupina_forms.SkupinaCreateForm(row)
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
                    row['skupina'] = skupina.pk
                    form = podskupina_forms.PodskupinaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_deli_skupine()

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

            return messages.success(
                request,
                "DELOVNI_NALOGI:DELO_VRSTA_SKLOP Število dodanih vnosov: %s" % (records_added)
            )

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

        def import_etaznalastnina_program():
            filename = os.path.abspath("eda5/templates/import/etazna_lastnina/program.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = ProgramCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "PROGRAM: Število dodanih vnosov: %s" % (records_added))

        def import_etaznalastnina_elaborat():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/etazna_lastnina/elaborat.csv")
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
                postna_stevilka = row['posta']
                program_oznaka = row['program']

                try:
                    program = Program.objects.get(oznaka=program_oznaka)
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)

                    row['posta'] = posta.pk
                    row['program'] = program.pk

                    form = LastniskaEnotaElaboratCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_etaznalastnina_program()
                    import_poste()
                    import_poste_tujina()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "ELABORAT LE: Število dodanih vnosov: %s" % (records_added))

        def import_etaznalastnina_interna():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/etazna_lastnina/interna.csv")
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
                elaborat_oznaka = row['elaborat']

                try:
                    elaborat = LastniskaEnotaElaborat.objects.get(oznaka=elaborat_oznaka)

                    row['elaborat'] = elaborat.pk

                    form = LastniskaEnotaInternaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_etaznalastnina_elaborat()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "INTERNA LE: Število dodanih vnosov: %s" % (records_added))

        def import_etaznalastnina_uporabno_dovoljenje():
            filename = os.path.abspath("eda5/templates/import/etazna_lastnina/uporabno_dovoljenje.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = UporabnoDovoljenjeCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "UPORABNO DOVOLJENJE: Število dodanih vnosov: %s" % (records_added))

        def import_etaznalastnina_interna_dodatno():
            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/etazna_lastnina/interna_dodatno.csv")
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
                interna_oznaka = row['interna']
                uporabno_dovoljenje_oznaka = row['uporabno_dovoljenje']
                lastnik_oznaka = row['lastnik']
                najemnik_oznaka = row['najemnik']
                placnik_oznaka = row['placnik']

                try:
                    interna = LastniskaEnotaInterna.objects.get(oznaka=interna_oznaka)
                    lastnik = SkupinaPartnerjev.objects.get(oznaka=lastnik_oznaka)
                    placnik = SkupinaPartnerjev.objects.get(oznaka=placnik_oznaka)

                    row['interna'] = interna.pk
                    row['lastnik'] = lastnik.pk
                    row['placnik'] = placnik.pk

                    if najemnik_oznaka:
                        najemnik = SkupinaPartnerjev.objects.get(oznaka=najemnik_oznaka)
                        row['najemnik'] = najemnik.pk
                    else:
                        row['najemnik'] = ""

                    if uporabno_dovoljenje_oznaka:
                        uporabno_dovoljenje = UporabnoDovoljenje.objects.get(oznaka=uporabno_dovoljenje_oznaka)
                        row['uporabno_dovoljenje'] = uporabno_dovoljenje.pk
                    else:
                        row['uporabno_dovoljenje'] = ""

                    form = InternaDodatnoCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_etaznalastnina_interna()
                    import_etaznalastnina_uporabno_dovoljenje()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "INTERNA-DODATNO LE: Število dodanih vnosov: %s" % (records_added))

        def import_katalog_tip_artikla():

            filename = os.path.abspath("eda5/templates/import/katalog/tip_artikla.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = TipArtiklaCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "KATALOG/ TIP ARTIKLA: Število dodanih vnosov: %s" % (records_added))

        def import_katalog_proizvajalec():

            filename = os.path.abspath("eda5/templates/import/katalog/proizvajalec.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = ProizvajalecCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "KATALOG/ PROIZVAJALEC: Število dodanih vnosov: %s" % (records_added))

        def import_katalog_model_artikla():
            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/katalog/model_artikla.csv")
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
                tip_artikla_oznaka = row['tip_artikla']
                proizvajalec_oznaka = row['proizvajalec']

                try:
                    tip_artikla = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)
                    proizvajalec = Proizvajalec.objects.get(oznaka=proizvajalec_oznaka)

                    row['tip_artikla'] = tip_artikla.pk
                    row['proizvajalec'] = proizvajalec.pk

                    form = ModelArtiklaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    import_katalog_proizvajalec()
                    import_katalog_tip_artikla()

            # na ekranu prikažem informacijo o številu uvozov
            return messages.success(request, "KATALOG/ MODEL ARTIKLA: Število dodanih vnosov: %s" % (records_added))


        def import_posta_skupina_dokumenta():

            filename = os.path.abspath("eda5/templates/import/posta/skupina_dokumenta.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = SkupinaDokumentaCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "POSTA/ SKUPINA_DOKUMENTA: Število dodanih vnosov: %s" % (records_added))

        def import_posta_vrsta_dokumenta():
            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/posta/vrsta_dokumenta.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # oznako skupine zamenjamo z ID skupine
                    skupina_oznaka = row['skupina']
                    skupina = SkupinaDokumenta.objects.get(oznaka=skupina_oznaka)
                    row['skupina'] = skupina.pk
                    form = VrstaDokumentaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                return messages.success(request, "POSTA/ VRSTA_DOKUMENTA: Število dodanih vnosov: %s" % (records_added))

            except:
                import_posta_skupina_dokumenta()

        ###############################################################################################################
        # PREDPISI ####################################################################################################
        ###############################################################################################################

        # PredpisSklop
        def import_predpisi_predpis_sklop():

            filename = os.path.abspath("eda5/templates/import/predpisi/predpis_sklop.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = PredpisSklopCreateForm(row)
                if form.is_valid():
                    print(row, "--> valid")
                    form.save()
                    records_added += 1
                else:
                    print(row, "--> invalid")

            return messages.success(request, "PREDPISI/ SKLOP: Število dodanih vnosov: %s" % (records_added))

        # PredpisPodsklop
        def import_predpisi_predpis_podsklop():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/predpisi/predpis_podsklop.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # oznako skupine zamenjamo z ID skupine
                    predpis_sklop_oznaka = row['predpis_sklop']
                    predpis_sklop = PredpisSklop.objects.get(oznaka=predpis_sklop_oznaka)
                    row['predpis_sklop'] = predpis_sklop.pk
                    form = PredpisPodsklopCreateForm(row)
                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "PREDPISI/ SKLOP: Število dodanih vnosov: %s" % (records_added))

            except:
                import_predpisi_predpis_sklop()
                import_predpisi_predpis_podsklop()

        # PredpisOpravilo
        def import_predpisi_predpis_opravilo():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/predpisi/predpis_opravilo.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # podsklop
                    predpis_podsklop_oznaka = row['predpis_podsklop']
                    predpis_podsklop = PredpisPodsklop.objects.get(oznaka=predpis_podsklop_oznaka)
                    row['predpis_podsklop'] = predpis_podsklop.pk

                    # predpis
                    row['predpis'] = None

                    form = PredpisOpraviloCreateForm(row)

                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "PREDPISI/ OPRAVILO: Število dodanih vnosov: %s" % (records_added))

            except:
                import_predpisi_predpis_podsklop()
                import_predpisi_predpis()

        # Predpis
        def import_predpisi_predpis():

            filename = os.path.abspath("eda5/templates/import/predpisi/predpis.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:
                form = PredpisCreateForm(row)

                if form.is_valid():
                    print(row, "--> valid")
                    form.save()
                    records_added += 1
                else:
                    print(row, "--> invalid")

            return messages.success(request, "PREDPISI/ PREDPIS: Število dodanih vnosov: %s" % (records_added))

        # Predpis-Opravilo ManyToMany
        def import_predpisi_opravila_many():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/predpisi/predpisi_opravila.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:
                    print(row)

                    # podsklop
                    predpis_opravilo_oznaka = row['predpis_opravilo']
                    predpis_oznaka = row['predpis']
                    print(predpis_opravilo_oznaka)
                    print(predpis_oznaka)
                    predpis_opravilo_obj = PredpisOpravilo.objects.get(oznaka=predpis_opravilo_oznaka)
                    print(predpis_opravilo_obj)

                    # predpis


                    predpis_obj = Predpis.objects.get(oznaka=predpis_oznaka)
                    print(predpis_obj)

                    predpis_opravilo_obj.predpis.add(predpis_obj)

                    records_added += 1
                    print(predpis_obj,"-->",predpis_opravilo_obj)

                return messages.success(request, "PREDPISI/ OPRAVILO: Število dodanih vnosov: %s" % (records_added))

            except:
                print("ZARADI NAPAK NE MOREM UVOZITI")


        # StevcnoStanje
        def import_stevcnostanje_stevec():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/stevcnostanje/stevcnostanje_stevci.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # podsklop
                    upravljavec_davcna = row['upravljavec']
                    upravljavec = Partner.objects.get(davcna_st=upravljavec_davcna)
                    row['upravljavec'] = upravljavec.pk

                    form = StevecCreateForm(row)

                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "STEVCNO STANJE/ STEVCI: Število dodanih vnosov: %s" % (records_added))

            except:
                import_partnerji()


        def import_stevcnostanje_stevecstatus():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/stevcnostanje/stevcnostanje_status.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # podsklop
                    stevec_oznaka = row['stevec']
                    stevec = Stevec.objects.get(oznaka=stevec_oznaka)
                    row['stevec'] = stevec.pk

                    form = StevecStatusCreateForm(row)

                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "STEVCNO STANJE/ STEVCI STATUS: Število dodanih vnosov: %s" % (records_added))

            except:
                import_stevcnostanje_stevec()


        def import_stevcnostanje_delilnik():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/stevcnostanje/stevcnostanje_delilniki.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # podsklop
                    stevec_oznaka = row['stevec']
                    stevec = Stevec.objects.get(oznaka=stevec_oznaka)
                    row['stevec'] = stevec.pk

                    form = DelilnikCreateForm(row)

                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "STEVCNO STANJE/ DELILNIKI: Število dodanih vnosov: %s" % (records_added))

            except:
                import_stevcnostanje_stevec()


        def import_stevcnostanje_odcitek():

            # uvozim datoteko .csv s podatki
            filename = os.path.abspath("eda5/templates/import/stevcnostanje/stevcnostanje_odcitki.csv")
            with open(filename, 'r') as file:
                vsebina = file.read()
            # parameter števila novih vnosov nastavim = 0
            records_added = 0
            # izdelam seznam podatkov
            rows = io.StringIO(vsebina)
            seznam = csv.DictReader(rows, delimiter=",")
            # iteriramo skozi seznam in vsakega poskušam dodati preko obrazca v bazo
            try:

                for row in seznam:

                    # podsklop
                    delilnik_oznaka = row['delilnik']
                    delilnik = Delilnik.objects.get(oznaka=delilnik_oznaka)
                    row['delilnik'] = delilnik.pk

                    form = OdcitekCreateForm(row)

                    if form.is_valid():
                        print(row, "--> valid")
                        form.save()
                        records_added += 1
                    else:
                        print(row, "--> invalid")

                return messages.success(request, "STEVCNO STANJE/ ODCITKI: Število dodanih vnosov: %s" % (records_added))

            except:
                import_stevcnostanje_delilnik()


            # na ekranu prikažem informacijo o številu uvozov

        if utiliti_uvoz_form.is_valid():

            if utiliti_uvoz_form.cleaned_data['utiliti'] is True:
                import_utility()

        if partnerji_uvoz_form.is_valid():

            if partnerji_uvoz_form.cleaned_data['poste'] is True:
                import_poste()

            if partnerji_uvoz_form.cleaned_data['poste_tujina'] is True:
                import_poste_tujina()

            if partnerji_uvoz_form.cleaned_data['banke'] is True:
                import_partnerji_banka()

            if partnerji_uvoz_form.cleaned_data['partnerji'] is True:
                import_partnerji()

            if partnerji_uvoz_form.cleaned_data['partnerji_edacenter'] is True:
                import_partnerji_edacenter()

            if partnerji_uvoz_form.cleaned_data['partnerji_edafm_update'] is True:
                partnerji_edafm_update()

        if deli_uvoz_form.is_valid():

            if deli_uvoz_form.cleaned_data['skupine_delov_stavbe'] is True:
                import_deli_podskupine()

        if racunovodstvo_uvoz_form.is_valid():

            if racunovodstvo_uvoz_form.cleaned_data['stroskovna_mesta'] is True:
                import_racunovodstvo_vrste_stroskov()

        if delovninalogi_uvoz_form.is_valid():

            if delovninalogi_uvoz_form.cleaned_data['vrste_del'] is True:
                import_delovninalog_delo_vrsta()

        if etaznalastnina_uvoz_form.is_valid():

            if etaznalastnina_uvoz_form.cleaned_data['etazna_lastnina'] is True:
                import_etaznalastnina_interna()

            if etaznalastnina_uvoz_form.cleaned_data['interna_dodatno'] is True:
                import_etaznalastnina_interna_dodatno()

            if etaznalastnina_uvoz_form.cleaned_data['uporabno_dovoljenje'] is True:
                import_etaznalastnina_uporabno_dovoljenje()

        if katalog_uvoz_form.is_valid():

            if katalog_uvoz_form.cleaned_data['tip_artikla'] is True:
                import_katalog_tip_artikla()

            if katalog_uvoz_form.cleaned_data['proizvajalec'] is True:
                import_katalog_proizvajalec()

            if katalog_uvoz_form.cleaned_data['model_artikla'] is True:
                import_katalog_model_artikla()

        if posta_uvoz_form.is_valid():

            if posta_uvoz_form.cleaned_data['vrsta_dokumenta'] is True:
                import_posta_vrsta_dokumenta()

        if predpisi_uvoz_form.is_valid():

            if predpisi_uvoz_form.cleaned_data['opravila'] is True:
                import_predpisi_predpis_opravilo()

            if predpisi_uvoz_form.cleaned_data['predpisi'] is True:
                import_predpisi_predpis()

            if predpisi_uvoz_form.cleaned_data['relacija_predpisi_opravila'] is True:
                import_predpisi_opravila_many()

        if stevcnostanje_uvoz_form.is_valid():

            if stevcnostanje_uvoz_form.cleaned_data['stevci'] is True:
                import_stevcnostanje_stevec()

            if stevcnostanje_uvoz_form.cleaned_data['stevci_status'] is True:
                import_stevcnostanje_stevecstatus()

            if stevcnostanje_uvoz_form.cleaned_data['delilniki'] is True:
                import_stevcnostanje_delilnik()

            if stevcnostanje_uvoz_form.cleaned_data['odcitki'] is True:
                import_stevcnostanje_odcitek()

        if moduli_uvoz_form.is_valid():

            if moduli_uvoz_form.cleaned_data['moduli'] is True:
                import_moduli()
                import_moduli_zavihki()


        return HttpResponseRedirect(reverse('moduli:import:form'))
