from django.test import TestCase
from django.core.urlresolvers import reverse

# factories
from eda5.arhiv.factories import ArhivFactory
from ..factories import KontrolaSpecifikacijaFactory

# models
from ..models import Aktivnost




class KontrolniListSpecifikacijaCreateViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        kontrola_specifikacija = KontrolaSpecifikacijaFactory()
        kontrola_specifikacija.save()


    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = '/moduli/kl/{}/specifikacija/create'.format(opraviloid)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_url_name(self):
        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'kontrolnilist/create.html')
