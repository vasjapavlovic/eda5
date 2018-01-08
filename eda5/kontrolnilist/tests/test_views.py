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
        url = '/moduli/kl/{}/specifikacija/create'.format(opraviloid)
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
