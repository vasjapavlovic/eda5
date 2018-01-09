from django.test import TestCase, Client
from django.test import RequestFactory
from django.core.urlresolvers import reverse

# factories
from eda5.arhiv.factories import ArhivFactory
from ..factories import KontrolaSpecifikacijaFactory
from eda5.users.factories import UserFactory

# models
from ..models import Aktivnost
from ..models import KontrolaSpecifikacija
from eda5.users.models import User
from eda5.delovninalogi.models import Opravilo

# Forms
from ..forms import AktivnostCreateForm
from ..forms import KontrolaSpecifikacijaFormSet




class KontrolniListSpecifikacijaCreateViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        kontrola_specifikacija = KontrolaSpecifikacijaFactory()
        kontrola_specifikacija.save()


        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        #user.set_password
        # print(user.password) --> pbkdf2_sha256$20000$3QQUNIB8CBsy$tCCokNu3NUoCtb95Thq2/uW7DP1vCPD+aZi7kc1Mwzw=


        # class UserFactory(factory.django.DjangoModelFactory):
        #
        #     class Meta:
        #         model = User
        #
        #
        #
        #     email = 'vaspav@vaspav.com'
        #     username = 'vaspav'
        #     password = 'medomedo8333333'
        #     is_superuser = True
        #     is_staff = True
        #     is_active = True
        # print(user.password) --> medomedo8333333



    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        self.client = Client()
        self.client.login(username='vaspav', password='medomedo')

        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = '/moduli/kl/opravilo/{0}/aktivnost/create'.format(opraviloid)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_url_name(self):
        self.client = Client()
        self.client.login(username='vaspav', password='medomedo')

        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client = Client()
        self.client.login(username='vaspav', password='medomedo')

        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'kontrolnilist/create.html')

    def test_redirect_if_not_loggedin(self):

        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk
        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_adds_data_if_all_ok(self):
        self.client = Client()
        self.client.login(username='vaspav', password='medomedo')


        aktivnost = Aktivnost.objects.first()
        opraviloid = aktivnost.opravilo.pk

        url = reverse('moduli:kontrolni_list:kontrolni_list_specifikacija_create', kwargs={'pk': opraviloid})

        data={
            'oznaka': 'ozn',
            'naziv': 'nzv',
            'kontrolaspecifikacija_set-TOTAL_FORMS': 1,
            'kontrolaspecifikacija_set-INITIAL_FORMS': 0,
            'kontrolaspecifikacija_set-0-oznaka': 'A1',
            'kontrolaspecifikacija_set-0-naziv': 'kontrola 1',
            'kontrolaspecifikacija_set-0-opis': 'opis 1',
            'kontrolaspecifikacija_set-0-vrednost_vrsta': 1,
        }

        response = self.client.post(url, data)
        aktivnost = Aktivnost.objects.get(oznaka='ozn')
        ks=KontrolaSpecifikacija.objects.filter(aktivnost=aktivnost)[0]
        self.assertEquals(aktivnost.oznaka, 'ozn')
        self.assertEquals(ks.oznaka, 'A1')


class KontrolniListSpecifikacijaUpdateViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        kontrola_specifikacija = KontrolaSpecifikacijaFactory()
        kontrola_specifikacija.save()


        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()


    def test_view_url_exists_at_desired_location(self):
        '''
        preverimo, da je url tak kot ga želimo
        '''
        self.client.login(username='vaspav', password='medomedo')
        aktivnost = Aktivnost.objects.first()

        url = '/moduli/kl/aktivnost/{0}/update'.format(aktivnost.pk)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)




    def test_views_loads_the_right_template(self):
        '''
        preverimo če se view loada na pravi strani in vrne status kodo 200
        '''
        self.client = Client()
        self.client.login(username='vaspav', password='medomedo')
        aktivnost = Aktivnost.objects.first()

        url = reverse('moduli:kontrolni_list:kontrolni_list_aktivnost_update', kwargs={'pk': aktivnost.pk})

        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('kontrolnilist/create.html')


    def test_view_updates_data(self):
        '''
        spremenimo podatke v kontroli specifikacije in preverimo
        ali so v bazi spremenjeni.
        '''

        self.client.login(username='vaspav', password='medomedo')
        aktivnost = Aktivnost.objects.first()
        url = reverse('moduli:kontrolni_list:kontrolni_list_aktivnost_update', kwargs={'pk': aktivnost.pk})
        response = self.client.get(url)

        # začasno lahko ponoviš ta test, da veš če je s testom kaj narobe
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('kontrolnilist/create.html')



        data = {
            'oznaka': 'ozn',
            'naziv': 'nzv',
            'kontrolaspecifikacija_set-TOTAL_FORMS': 1,
            'kontrolaspecifikacija_set-INITIAL_FORMS': 0,
            'kontrolaspecifikacija_set-0-oznaka': 'A1',
            'kontrolaspecifikacija_set-0-naziv': 'kontrola 1',
            'kontrolaspecifikacija_set-0-opis': 'opis 1',
            'kontrolaspecifikacija_set-0-vrednost_vrsta': 1,
        }

        # izvršimo update
        response = self.client.post(url, data)

        # pridobimo podatke
        aktivnost_potem = Aktivnost.objects.get(id=aktivnost.pk)
        ks = KontrolaSpecifikacija.objects.filter(aktivnost=aktivnost)
        ks_0 = ks[0]

        self.assertTrue(KontrolaSpecifikacija.objects.filter(oznaka='A1').exists())

        self.assertEquals(aktivnost_potem.oznaka, 'ozn')
        self.assertEquals(ks_0.oznaka, 'A1')

        self.assertEquals(Aktivnost.objects.filter().count(), 1)

    def test_view_dodamo_novo_kontrolo(self):
        self.client.login(username='vaspav', password='medomedo')

        aktivnost = Aktivnost.objects.filter()
        # preverimo, da obstaja samo ena aktivnost
        self.assertEquals(aktivnost.count(), 1)

        # če obstaja ena aktivnost jo izberemo
        if aktivnost.count() == 1:
            aktivnost = aktivnost.first()

        # preverimo, da obstaja samo ena kontrola pod to aktivnosti
        ks_0 = KontrolaSpecifikacija.objects.filter(aktivnost=aktivnost)
        self.assertEquals(ks_0.count(), 1)

        # pripravimo podatke, ki jih bomo spremenili
        # kontroli ks_0 popravimo oznako na 'KS_0'
        # dodamo novo kontrolo z oznako 'KS_1'

        url = reverse('moduli:kontrolni_list:kontrolni_list_aktivnost_update', kwargs={'pk': aktivnost.pk})


        data = {
            'oznaka': 'OZNAKA',
            'naziv': 'NAZIV',
            'kontrolaspecifikacija_set-TOTAL_FORMS': 1,
            'kontrolaspecifikacija_set-INITIAL_FORMS': 0,
            'kontrolaspecifikacija_set-0-oznaka': 'KS_0',
            'kontrolaspecifikacija_set-0-naziv': 'A1',
            'kontrolaspecifikacija_set-0-opis': 'ass',
            'kontrolaspecifikacija_set-0-vrednost_vrsta': 1,
        }

        # izvršimo post
        response = self.client.post(url, data)

        # še na drugi način če deluje
        self.assertTrue(KontrolaSpecifikacija.objects.filter(oznaka='KS_0').exists())


        # koliko kontrol ima obstoječa aktivnost
        ks = KontrolaSpecifikacija.objects.filter()
        self.assertEquals(
            ks.count(),
            2
        )

    def test_view_spremenimo_kontrolo_1(self):
        self.client.login(username='vaspav', password='medomedo')

        aktivnost = Aktivnost.objects.filter()
        # preverimo, da obstaja samo ena aktivnost
        self.assertEquals(aktivnost.count(), 1)

        # če obstaja ena aktivnost jo izberemo
        if aktivnost.count() == 1:
            aktivnost = aktivnost.first()

        # preverimo, da obstaja samo ena kontrola pod to aktivnosti
        ks = KontrolaSpecifikacija.objects.filter(aktivnost=aktivnost)
        self.assertEquals(ks.count(), 1)

        ks_0 = ks[0]

        # pripravimo podatke, ki jih bomo spremenili
        # kontroli ks_0 popravimo oznako na 'KS_0'
        # dodamo novo kontrolo z oznako 'KS_1'

        url = reverse('moduli:kontrolni_list:kontrolni_list_aktivnost_update', kwargs={'pk': aktivnost.pk})


        data = {
            'oznaka': 'OZNAKA',
            'naziv': 'NAZIV',
            'kontrolaspecifikacija_set-TOTAL_FORMS': 2,
            'kontrolaspecifikacija_set-INITIAL_FORMS': 1,
            'kontrolaspecifikacija_set-0-id': ks_0.pk,
            'kontrolaspecifikacija_set-0-oznaka': 'KS_0',
            'kontrolaspecifikacija_set-0-naziv': 'A1',
            'kontrolaspecifikacija_set-0-opis': 'ass',
            'kontrolaspecifikacija_set-0-vrednost_vrsta': 1,
            'kontrolaspecifikacija_set-1-oznaka': 'KS_1',
            'kontrolaspecifikacija_set-1-naziv': 'A1',
            'kontrolaspecifikacija_set-1-opis': 'ass',
            'kontrolaspecifikacija_set-1-vrednost_vrsta': 1,
        }



        response = self.client.post(url, data)

        self.assertEquals(Aktivnost.objects.first().oznaka, 'OZNAKA')

        # še na drugi način če deluje
        self.assertTrue(KontrolaSpecifikacija.objects.filter(oznaka='KS_0').exists())

        # ks_0 id je enak novemu id
        self.assertEquals(ks_0.id, KontrolaSpecifikacija.objects.filter(oznaka='KS_0')[0].id)

        # KS_5 ga ni v bazi
        self.assertFalse(KontrolaSpecifikacija.objects.filter(oznaka='KS_5').exists())


        self.assertTrue(KontrolaSpecifikacija.objects.filter(oznaka='KS_1').exists())

        # koliko kontrol ima obstoječa aktivnost
        ks = KontrolaSpecifikacija.objects.filter()
        self.assertEquals(
            ks.count(),
            2
        )
