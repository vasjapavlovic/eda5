from django.core.urlresolvers import reverse
from django.test import TestCase


class TestPredajaLastnineHomeView(TestCase):
    fixutres = [
        'predaja_lastnine_partnerji.json',
        'predaja_lastnine_etazna_lastnina.json',
        'predaja_lastnine_views_testdata.json',
    ]

    def setUp(self):
        pass


    def test_home_page_shows(self):
        resp = self.client.get(reverse('moduli:predaja_lastnine:home'))
        self.assertEqual(
            resp.status_code,
            200
        )