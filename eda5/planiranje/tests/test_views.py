from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from ..models import Plan, PlanAktivnost, PlanKontrolaSkupina

from ..factories import PlanFactory, PlaniranoOpraviloFactory, PlanAktivnostFactory, PlanKontrolaSkupinaFactory
from eda5.users.factories import UserFactory



class PlanUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        plan = PlanFactory()
        plan.save()


    def test_url_path(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = '/moduli/planiranje/plan/{0}/update'.format(plan.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_url_namespace(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_update', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_correct_template(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_update', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/planiranje/plan/update.html')

    def test_redirect_if_not_logged_in(self):
        model_object = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_update', kwargs={'pk': model_object.pk })
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 302)
        self.assertTemplateUsed('account/login.html')


class PlanAktivnostCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        # skupine kontrol se dodajajo pod aktivnostih
        plan = PlanFactory()
        plan.save()


    def test_url_path(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = '/moduli/planiranje/plan/{0}/plan-aktivnost/create'.format(plan.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_url_namespace(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_aktivnost_create', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_correct_template(self):
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_aktivnost_create', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/planiranje/plan_aktivnost/create.html')

    def test_redirect_if_not_logged_in(self):
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_aktivnost_create', kwargs={'pk': plan.pk })
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 302)
        self.assertTemplateUsed('account/login.html')


class PlanKontrolaSkupinaCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        # skupine kontrol se dodajajo pod aktivnostih
        pa = PlanAktivnostFactory()
        pa.save()


    def test_url_path(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pa = PlanAktivnost.objects.first()
        url = '/moduli/planiranje/plan-aktivnost/{0}/plan-kontrola-skupina/create'.format(pa.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)


    def test_url_namespace(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pa = PlanAktivnost.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_skupina_create', kwargs={'pk': pa.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_correct_template(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pa = PlanAktivnost.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_skupina_create', kwargs={'pk': pa.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/planiranje/plan_kontrola_skupina/create.html')

    def test_redirect_if_not_logged_in(self):
        pa = PlanAktivnost.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_skupina_create', kwargs={'pk': pa.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 302)
        self.assertTemplateUsed('account/login.html')


class PlanKontrolaSpecifikacijaCreateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        # skupine kontrol se dodajajo pod aktivnostih
        pks = PlanKontrolaSkupinaFactory()
        pks.save()


    def test_url_path(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pks = PlanKontrolaSkupina.objects.first()
        url = '/moduli/planiranje/plan-kontrola-skupina/{0}/plan-kontrola-specifikacija/create'.format(pks.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)


    def test_url_namespace(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pks = PlanKontrolaSkupina.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_specifikacija_create', kwargs={'pk': pks.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_correct_template(self):
        login = self.client.login(username='vaspav', password='medomedo')
        pks = PlanKontrolaSkupina.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_specifikacija_create', kwargs={'pk': pks.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed('/planiranje/plan_kontrola_specifikacija/create.html')

    def test_redirect_if_not_logged_in(self):
        pks = PlanKontrolaSkupina.objects.first()
        url = reverse('moduli:planiranje:plan_kontrola_specifikacija_create', kwargs={'pk': pks.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 302)
        self.assertTemplateUsed('account/login.html')



class PlanOpraviloCreateView(TestCase):
    pass
#
#     @classmethod
#     def setUpTestData(cls):
#
#         user = UserFactory()
#         user.save()
#         user.set_password('medomedo')
#         user.save()
#
#
#     def test_url_path(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = ''.format()
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 200)
#
#
#     def test_url_namespace(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 200)
#
#     def test_correct_template(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertTemplateUsed('/planiranje/plan/update.html')
#
#     def test_redirect_if_not_logged_in(self):
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 302)
#         self.assertTemplateUsed('login.html')





class PlanPrintViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = UserFactory()
        user.save()
        user.set_password('medomedo')
        user.save()

        plan = PlanFactory()
        plan.save()

        planirano_opravilo = PlaniranoOpraviloFactory(plan=plan)
        planirano_opravilo.save()

    def test_url_path(self):
        self.client = Client()
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = '/moduli/planiranje/plan/{0}/print'.format(plan.pk)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_url_namespace(self):
        self.client = Client()
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_print', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_correct_template(self):
        self.client = Client()
        login = self.client.login(username='vaspav', password='medomedo')
        plan = Plan.objects.first()
        url = reverse('moduli:planiranje:plan_print', kwargs={'pk': plan.pk})
        resp = self.client.get(url)
        self.assertTemplateUsed(resp, 'planiranje/plan/plan_print.html')


    def test_post_context_data(self):
        pass

    def test_ordering(self):
        pass
