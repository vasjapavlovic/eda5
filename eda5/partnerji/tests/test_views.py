from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Partner, TRRacun, Posta


class PartnerHomeViewTestCase(TestCase):

    def test_PartnerHomeView(self):
        resp = self.client.get(reverse('moduli:partnerji:home'))
        self.assertEqual(resp.status_code, 200)


class PartnerListViewTestCase(TestCase):

    fixtures = ['partnerji_views_testdata.json']

    def test_PartnerListView(self):
        resp = self.client.get(reverse('moduli:partnerji:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('object_list' in resp.context)

        partner_1 = resp.context['object_list'][0]
        self.assertEqual(partner_1.pk, 1)
        self.assertEqual(partner_1.kratko_ime, 'EDAFM d.o.o.')

        trr_1 = partner_1.trracun_set.all()
        self.assertEqual(trr_1[0].iban, "SI56047500002032492")

        # preverimo relacijo z banko preko trračuna
        banka_trr_1 = trr_1[0].banka.partner.pk
        partner_3 = resp.context['object_list'][2]
        self.assertEqual(partner_3.pk, banka_trr_1)


class PartnerCreateViewTestCase(TestCase):

    fixtures = ['partnerji_views_testdata.json']

    def test_dodam_novega_partnerja(self):

        # preverimo da je število partnerjev 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

        # vnesemo novega partnerja
        posta = Posta.objects.get(postna_stevilka="5000")
        self.assertEqual(posta.naziv, "Nova Gorica")  # samo preverim, da pošta obstaja
        resp = self.client.post(reverse('moduli:partnerji:create'),
            {
                'is_pravnaoseba': True,
                'davcni_zavezanec': True,
                'davcna_st': "12345",
                'maticna_st': "34567",
                'dolgo_ime': "Testni Partner Dolgo Ime",
                'kratko_ime': "Testni Partner",
                'naslov': "testni naslov",
                'posta': posta.pk,
            }
        )
        # po končanem vnosu --> Preusmeritev : Nujno pri POST
        self.assertEqual(resp.status_code, 302)
        # lokacija redirecta --> PartnerDetailView
        self.assertEqual(
            resp["Location"],
            "http://testserver" + reverse('moduli:partnerji:detail', kwargs={"pk": 4})
        )

        # preverimo, da je število parnerjev + 1
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 4)

    def test_partnerja_z_davcno_ki_je_ze_v_bazi_ne_doda(self):

        # preverimo da je število partnerjev 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

        # definiram partnerja z novo davčno številko
        davcna_st = "97041823"
        maticna_st = "12344"
        dolgo_ime = "nov partner z novo dalčno dolgo ime"
        kratko_ime = "nov partner z novo davcno"
        naslov = "naslov partnerja z novo davčno številko"
        posta = 1
        is_pravnaoseba = True
        davcni_zavezanec = False

        # preverimo, da davčna številka že obstaja
        partnerji = Partner.objects.all()
        self.assertTrue(any(davcna_st == partner.davcna_st for partner in partnerji))

        # samo preverim, da pošta obstaja
        posta = Posta.objects.filter(id=posta)
        self.assertEqual(posta.count(), 1)

        # dodamo novega partnerja z novo_davčno_številko
        resp = self.client.post(reverse('moduli:partnerji:create'),
            {
                'is_pravnaoseba': is_pravnaoseba,
                'davcni_zavezanec': davcni_zavezanec,
                'davcna_st': davcna_st,
                'maticna_st': maticna_st,
                'dolgo_ime': dolgo_ime,
                'kratko_ime': kratko_ime,
                'naslov': naslov,
                'posta': posta,
            }
        )

        # preverimo da je število partnerjev še vedno = 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

    def test_partnerja_z_maticno_ki_je_ze_v_bazi_ne_doda(self):

        # preverimo da je število partnerjev 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

        # definiram partnerja z novo davčno številko
        davcna_st = "098765"
        maticna_st = "6163157000"
        dolgo_ime = "nov partner z novo dalčno dolgo ime"
        kratko_ime = "nov partner z novo davcno"
        naslov = "naslov partnerja z novo davčno številko"
        posta = 1
        is_pravnaoseba = True
        davcni_zavezanec = False

        # preverimo, da davčna številka že obstaja
        partnerji = Partner.objects.all()
        self.assertTrue(any(maticna_st == partner.maticna_st for partner in partnerji))

        # samo preverim, da pošta obstaja
        posta = Posta.objects.filter(id=posta)
        self.assertEqual(posta.count(), 1)

        # dodamo novega partnerja z novo_davčno_številko
        resp = self.client.post(reverse('moduli:partnerji:create'),
            {
                'is_pravnaoseba': is_pravnaoseba,
                'davcni_zavezanec': davcni_zavezanec,
                'davcna_st': davcna_st,
                'maticna_st': maticna_st,
                'dolgo_ime': dolgo_ime,
                'kratko_ime': kratko_ime,
                'naslov': naslov,
                'posta': posta,
            }
        )

        # preverimo da je število partnerjev še vedno = 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

    def test_brez_vpisa_davcne_stevilke_partnerja_ne_doda(self):

        # preverimo da je število partnerjev 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)

        # definiram partnerja z novo davčno številko
        davcna_st = ""
        maticna_st = "6163157000"
        dolgo_ime = "nov partner z novo dalčno dolgo ime"
        kratko_ime = "nov partner z novo davcno"
        naslov = "naslov partnerja z novo davčno številko"
        posta = 1
        is_pravnaoseba = True
        davcni_zavezanec = False

        # samo preverim, da pošta obstaja
        posta = Posta.objects.filter(id=posta)
        self.assertEqual(posta.count(), 1)

        # dodamo novega partnerja z novo_davčno_številko
        resp = self.client.post(reverse('moduli:partnerji:create'),
            {
                'is_pravnaoseba': is_pravnaoseba,
                'davcni_zavezanec': davcni_zavezanec,
                'davcna_st': davcna_st,
                'maticna_st': maticna_st,
                'dolgo_ime': dolgo_ime,
                'kratko_ime': kratko_ime,
                'naslov': naslov,
                'posta': posta,
            }
        )

        # preverimo da je število partnerjev še vedno = 3
        stevilo_partnerjev = Partner.objects.all().count()
        self.assertEqual(stevilo_partnerjev, 3)


class PartnerDetailViewTestCase(TestCase):

    fixtures = ['partnerji_views_testdata.json']

    def test_partner_obstaja_vrne_status_200(self):
        # če partner obstaja 
        resp = self.client.get(reverse('moduli:partnerji:detail', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context, 'object')
        self.assertEqual(resp.context['object'].kratko_ime, 'EDAFM d.o.o.')

    def test_partner_ne_obstaja_vrne_status_404(self):
        # če partner ne obstaja 
        resp = self.client.get(reverse('moduli:partnerji:detail', kwargs={'pk': 100}))
        self.assertEqual(resp.status_code, 404)  # vrne napako = Page Not Found

    def test_partneru_lahko_dodamo_trr(self):
        partner_1 = Partner.objects.get(pk=1)
        # preverimo da je kratko_ime partnerja_1 = EDAFM d.o.o.
        self.assertEqual(partner_1.kratko_ime, "EDAFM d.o.o.")
        # kontrola: partner ima samo en (1) račun
        self.assertEqual(partner_1.trracun_set.all().count(), 1)
        # dodamo TRR račun
        resp = self.client.post(reverse('moduli:partnerji:detail', kwargs={'pk': 1}),
            {
                'iban': 'TESTIBAN',
                'banka': 2,
                'partner': partner_1.pk,
            }
        )
        # kontrola: partner ima dva (2) računa
        self.assertEqual(partner_1.trracun_set.all().count(), 2)

    def test_partnerju_ne_morem_dodati_trr_katerega_iban_obstaja(self):
        partner_1 = Partner.objects.get(pk=1)
        # preverimo da je kratko_ime partnerja_1 = EDAFM d.o.o.
        self.assertEqual(partner_1.kratko_ime, "EDAFM d.o.o.")
        # kontrola: ima že en račun
        self.assertEqual(partner_1.trracun_set.filter(iban="SI56047500002032492").count(), 1)
        # poskušamo dodati še enkrat že obstoječ račun --> ga ne sme vnesti
        resp = self.client.post(reverse('moduli:partnerji:detail', kwargs={'pk': 1}),
            {
                'iban': 'SI56047500002032492',
                'banka': 2,
                'partner': partner_1.pk,
            }
        )
        # kontrola: partner ima dva (2) računa
        self.assertEqual(partner_1.trracun_set.all().count(), 1)

