from django.test import TestCase

from ..factories import VzorecOpravilaFactory
from eda5.arhiv.factories import ArhivFactory
from eda5.kontrolnilist.factories import AktivnostFactory


from ..models import VzorecOpravila



class VzorecOpravilaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        arhiv = ArhivFactory()
        arhiv.save()

        akt = AktivnostFactory()
        akt.save()

        vo = VzorecOpravilaFactory(aktivnost=[akt,])
        vo.save()




    def test_field_planirano_opravilo_label(self):
        vo = VzorecOpravila.objects.first()
        label = vo._meta.get_field('planirano_opravilo').verbose_name
        self.assertEquals(label, 'planirano opravilo')

    def test_field_vrsta_stroska_label(self):
        vo = VzorecOpravila.objects.first()
        label = vo._meta.get_field('vrsta_stroska').verbose_name
        self.assertEquals(label, 'stroškovno mesto')

    def test_field_narocilo_label(self):
        vo = VzorecOpravila.objects.first()
        label = vo._meta.get_field('narocilo').verbose_name
        self.assertEquals(label, 'naročilo')

    def test_field_aktivnost_label(self):
        vo = VzorecOpravila.objects.first()
        label = vo._meta.get_field('aktivnost').verbose_name
        self.assertEquals(label, 'aktivnost')
