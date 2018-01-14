from django.test import TestCase



class VzorecOpravilaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass


    def test_field_aktivnost(self):
        ks = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('aktivnost').verbose_name
        self.assertEquals(result, 'aktivnost')
