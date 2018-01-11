from django.core.urlresolvers import reverse
from django.test import TestCase

# Models
from ..models import DelovniNalog
from ..models import Opravilo
from eda5.kontrolnilist.models import Aktivnost
from eda5.kontrolnilist.models import KontrolaSpecifikacija
from eda5.kontrolnilist.models import KontrolaVrednost
from eda5.kontrolnilist.models import KontrolaSpecifikacijaOpcijaSelect
from eda5.moduli.models import Zavihek

# factories
from ..factories import DelovniNalogFactory
from ..factories import OpraviloFactory
from eda5.arhiv.factories import ArhivFactory
from eda5.kontrolnilist.factories import KontrolaSpecifikacijaFactory
from eda5.kontrolnilist.factories import KontrolaSpecifikacijaOpcijaSelectFactory
from eda5.kontrolnilist.factories import KontrolaVrednostFactory
from eda5.moduli.factories import ZavihekFactory
from eda5.users.factories import UserFactory



class OpraviloDetailViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):

        arhiv = ArhivFactory()
        arhiv.save()

        zavihek = ZavihekFactory(oznaka='OPRAVILO_DETAIL')
        zavihek.save()

        #opravilo = OpraviloFactory()
        #opravilo.save()


        kontrola_specifikacija = KontrolaSpecifikacijaFactory(
            oznaka='KS_1_AKT1' ,aktivnost__oznaka='AKT1')
        kontrola_specifikacija.save()

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()


    def test_view_url_path(self):
        self.client.login(username='vaspav', password='medomedo')

        opravilo = Opravilo.objects.first()

        url = '/moduli/delovninalogi/opravila/{0}/detail'.format(opravilo.pk)

        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_view_namspace(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()
        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_view_loads_the_right_template(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()
        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/delovninalogi/opravilo/detail/base.html')

    def test_context_delovninalogi_list(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()
        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        # dobim ven seznam delovnih nalogov
        context = resp.context
        seznam_dn = context['delovninalog_list']
        dn_object = DelovniNalog.objects.filter(opravilo=opravilo).first()
        self.assertTrue(any(dn == dn_object for dn in seznam_dn))

    def test_context_kontrola_list(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()
        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        # seznam kontrolni list
        context = resp.context
        kontrola_list = context['kontrola_list']
        aktivnost = Aktivnost.objects.filter(opravilo=opravilo).first()
        kontrola_object = KontrolaSpecifikacija.objects.filter(aktivnost=aktivnost).first()
        self.assertTrue(any(kontrola_object == kontrola  for kontrola in kontrola_list))

    def test_contex_kontrola_list_ordered_by_aktivnost(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()

        # dodamo še dve kontroli
        kontrola_specifikacija = KontrolaSpecifikacijaFactory(
            oznaka='KS_1_AKT3' ,aktivnost__oznaka='AKT3', aktivnost__opravilo=opravilo)
        kontrola_specifikacija.save()

        kontrola_specifikacija = KontrolaSpecifikacijaFactory(
            oznaka='KS_1_AKT2' ,aktivnost__oznaka='AKT2', aktivnost__opravilo=opravilo)
        kontrola_specifikacija.save()

        kontrola_specifikacija = KontrolaSpecifikacijaFactory(
            oznaka='KS_2_AKT2' ,aktivnost__oznaka='AKT2', aktivnost__opravilo=opravilo)
        kontrola_specifikacija.save()

        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        # seznam kontrolni list
        context = resp.context
        kontrola_list = context['kontrola_list']

        # izpis kontrol po željenem vrstnem redu
        # AKT1
        #   K1
        #   K2
        # AKT2
        #   K1
        #   K2
        # AKT3
        #   K1
        #   K2
        ks_1 = kontrola_list[0]
        ks_2 = kontrola_list[1]
        ks_3 = kontrola_list[2]
        ks_4 = kontrola_list[3]

        self.assertEquals(ks_1.oznaka, 'KS_1_AKT1')
        self.assertEquals(ks_2.oznaka, 'KS_1_AKT2')
        self.assertEquals(ks_3.oznaka, 'KS_2_AKT2')
        self.assertEquals(ks_4.oznaka, 'KS_1_AKT3')


class DelovniNalogDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        arhiv = ArhivFactory()
        arhiv.save()

        zavihek = ZavihekFactory(oznaka='DN_DETAIL')
        zavihek.save()

        kontrola_vrednost = KontrolaVrednostFactory()
        kontrola_vrednost.save()

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()


    def test_view_url_path(self):
        self.client.login(username='vaspav', password='medomedo')
        dn = DelovniNalog.objects.first()
        url = '/moduli/delovninalogi/dn/{0}/detail'.format(dn.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_view_namspace(self):
        self.client.login(username='vaspav', password='medomedo')
        dn = DelovniNalog.objects.first()
        url = reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_view_loads_the_right_template(self):
        self.client.login(username='vaspav', password='medomedo')
        dn = DelovniNalog.objects.first()
        url = reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/delovninalogi/delovninalog/detail/base.html')



    # def test_specifikacija_vrednost_vrsta_select_ponudi_izbiro(self):
    #     self.client.login(username='vaspav', password='medomedo')
    #
    #     # vnesemo testne podatke
    #     # izdelamo specifikacijo
    #     ks = KontrolaSpecifikacijaFactory(oznaka="KS_1", vrednost_vrsta=3)
    #     ks.save()
    #     ks_1 = KontrolaSpecifikacija.objects.get(oznaka='KS_1')
    #
    #     # opcije za izbiro
    #     os_ks_1 = KontrolaSpecifikacijaOpcijaSelectFactory(oznaka='O_1', naziv='opcija 1' , kontrola_specifikacija=ks_1)
    #     os_ks_1.save()
    #     os_ks_2 = KontrolaSpecifikacijaOpcijaSelectFactory(oznaka='O_2', naziv='opcija 2',  kontrola_specifikacija=ks_1)
    #     os_ks_2.save()
    #     os_ks_3 = KontrolaSpecifikacijaOpcijaSelectFactory(oznaka='O_3', naziv='opcija 3',  kontrola_specifikacija=ks_1)
    #     os_ks_3.save()
    #
    #     # izdelamo vrednost iz specifikacija 1
    #     kv_1 = KontrolaVrednostFactory(oznaka='KV_1' , kontrola_specifikacija=ks_1)
    #     kv_1.save()
    #
    #     url = reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': kv_1.delovni_nalog.id})
    #     resp = self.client.get(url)
    #
    #     context = resp.context
    #     formset = context['kontrola_vrednost_update_formset']
    #     #print(formset[0].instance.vrednost_select)
    #
    #     form = formset.forms[0]
    #
    #     field_vrednost_select = form['vrednost_select']
    #     self.fail("dokončaj test")
