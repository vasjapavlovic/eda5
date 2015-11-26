from django import forms
from django.test import TestCase
from ..forms import PartnerCreateForm
from ..models import Partner, Posta


class PartnerCreateFormTest(TestCase):
    fixtures = ['partnerji_forms_testdata.json']

    def setUp(self):
        super(PartnerCreateFormTest, self).setUp()
        self.posta_1 = Posta.objects.get(postna_stevilka="5000")


    # def test_init(self):
    #     # Test a failed init without data.
    #     self.assertRaises(KeyError, PartnerCreateForm)

    #     # Test a failed init with data.
    #     self.assertRaises(KeyError, PartnerCreateForm, {})

    def test_vnos_pravilnih_podatkov(self):

        # vhodni podatki
        is_pravnaoseba = True
        davcni_zavezanec = True
        davcna_st = '12345'
        maticna_st = '34567'
        dolgo_ime = 'Testni Partner Dolgo Ime'
        kratko_ime = 'Testni Partner'
        naslov = 'testni naslov'
        posta = self.posta_1.pk


        form = PartnerCreateForm(
            {
                'is_pravnaoseba': is_pravnaoseba,
                'davcni_zavezanec': davcni_zavezanec,
                'davcna_st': davcna_st,
                'maticna_st': maticna_st,
                'dolgo_ime': dolgo_ime,
                'kratko_ime': kratko_ime,
                'naslov': naslov,
                'posta': self.posta_1.pk,
            }
        )

        self.assertTrue(form.is_valid())
        partner = form.save()
        self.assertEqual(partner.is_pravnaoseba, is_pravnaoseba)
        self.assertEqual(partner.davcni_zavezanec, davcni_zavezanec)
        self.assertEqual(partner.davcna_st, davcna_st)
        self.assertEqual(partner.maticna_st, maticna_st)
        self.assertEqual(partner.dolgo_ime, dolgo_ime)
        self.assertEqual(partner.kratko_ime, kratko_ime)
        self.assertEqual(partner.naslov, naslov)
        self.assertEqual(partner.posta.pk, posta)