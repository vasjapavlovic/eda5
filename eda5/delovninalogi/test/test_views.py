from django.core.urlresolvers import reverse
from django.test import TestCase

# Models
from ..models import DelovniNalog
from ..models import Opravilo
from eda5.kontrolnilist.models import Aktivnost
from eda5.kontrolnilist.models import KontrolaSpecifikacija
from eda5.moduli.models import Zavihek

# factories
from ..factories import DelovniNalogFactory
from ..factories import OpraviloFactory
from eda5.arhiv.factories import ArhivFactory
from eda5.kontrolnilist.factories import KontrolaSpecifikacijaFactory
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

        dn = DelovniNalogFactory()
        dn.save()

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

    def test_formset_for_kontrola_vrednost_input_data_in_context(self):
        self.client.login(username='vaspav', password='medomedo')
        dn = DelovniNalog.objects.first()
        url = reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.id})
        resp = self.client.get(url)

        context = resp.context
        formset = context['kontrola_vrednost_create_formset']
        form = formset.form
        field_vrednost_check = form['vrednost_check']
        vrednost = field_vrednost_check.value()
        self.assertEquals(vrednost, False)
