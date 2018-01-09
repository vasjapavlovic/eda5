from django.core.urlresolvers import reverse
from django.test import TestCase

# Models
from ..models import Opravilo
from eda5.moduli.models import Zavihek


# factories
from ..factories import OpraviloFactory
from eda5.arhiv.factories import ArhivFactory
from eda5.users.factories import UserFactory
from eda5.moduli.factories import ZavihekFactory


class OpraviloDetailViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):

        arhiv = ArhivFactory()
        arhiv.save()

        zavihek = ZavihekFactory(oznaka='OPRAVILO_DETAIL')
        zavihek.save()

        opravilo = OpraviloFactory()
        opravilo.save()


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


    def test_views_loads_the_right_template(self):
        self.client.login(username='vaspav', password='medomedo')
        opravilo = Opravilo.objects.first()
        url = reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/delovninalogi/opravilo/detail/base.html')
