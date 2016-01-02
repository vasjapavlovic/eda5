from django.core.urlresolvers import reverse
from django.test import TestCase


class PredajaLastnineHomeViewTest(TestCase):
    fixutres = [
        'predaja_lastnine_partnerji.json',
        'predaja_lastnine_etazna_lastnina.json',
        'predaja_lastnine_views_testdata.json',
    ]

    def setUp(self):
        pass

    def test_home_page_shows(self):
        resp = self.client.get(reverse('moduli:predaja_lastnine:home'))
        self.assertEqual(resp.status_code, 200)


class PredajaListViewTest(TestCase):
    fixutres = [
        'predaja_lastnine_partnerji.json',
        'predaja_lastnine_etazna_lastnina.json',
        'predaja_lastnine_views_testdata.json',
    ]

    def setUp(self):
        pass

    def test_stran_se_prikaze_v_streznem_htmlju(self):
        response = self.client.get(reverse('moduli:predaja_lastnine:predaja_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "predaja_lastnine/predajalastnine/list.html")

    def test_stran_ima_ustrezne_parametre(self):
        # parameter object_list (seznam vnos)
        resp = self.client.get(reverse('moduli:predaja_lastnine:predaja_list'))

        self.assertTrue(resp.context, "object_list")


class PredajaCreateViewTest(TestCase):
    fixutres = [
        'predaja_lastnine_partnerji.json',
        'predaja_lastnine_etazna_lastnina.json',
        'predaja_lastnine_views_testdata.json',
    ]

    def setUp(self):
        pass

    def test_stran_se_prikaze(self):
        response = self.client.get(reverse('moduli:predaja_lastnine:predaja_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "predaja_lastnine/predajalastnine/create.html")
