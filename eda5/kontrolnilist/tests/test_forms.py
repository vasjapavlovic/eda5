from django.test import TestCase

from ..models import KontrolaVrednost

from ..forms import AktivnostCreateForm
from ..forms import KontrolaSpecifikacijaCreateForm
from ..forms import KontrolaVrednostUpdateFormSetOblika01

from ..factories import KontrolaVrednostFactory
from eda5.arhiv.factories import ArhivFactory


class AktivnostCreateFormTest(TestCase):


    def form_data(self, oznaka, naziv, opis):

        return AktivnostCreateForm(
            data={
                'oznaka': oznaka,
                'naziv': naziv,
                'opis': opis,
                'form-TOTAL_FORMS': 1,
                'form-INITIAL_FORMS': 0,
                'form-0-oznaka': oznaka,
                'form-0-naziv': naziv,
            }

        )

    def test_valid_data(self):
        form = self.form_data('oznaka1', 'naziv1', 'opis1')
        self.assertTrue(form.is_valid())

    def test_missing_naziv(self):
        form = self.form_data('oznaka1', '', 'opis1')
        errors = form['naziv'].errors.as_data()
        self.assertEquals(len(errors), 1)
        self.assertEquals(errors[0].code, 'required')

    def test_brez_oznake_lahko(self):
        form = self.form_data('', 'naziv1', 'opis1')
        self.assertTrue(form.is_valid())

    def test_brez_opisa_lahko(self):
        form = self.form_data('oznaka1', 'naziv1', '')
        self.assertTrue(form.is_valid())

    def test_brez_oznake_in_opisa_lahko(self):
        form = self.form_data('', 'naziv1', '')
        self.assertTrue(form.is_valid())




class KontrolaSpecifikacijaCreateFormTest(TestCase):

    def setUp(self):
        pass

    def form_data(self, oznaka, naziv, opis, vrednost_vrsta):
        return KontrolaSpecifikacijaCreateForm(
            data={
                'oznaka': oznaka,
                'naziv': naziv,
                'opis': opis,
                'vrednost_vrsta': vrednost_vrsta,
            }
        )


    def test_valid_data(self):
        form = self.form_data('oznaka1', 'naziv1', 'opis1', 2)
        self.assertTrue(form.is_valid())



class KontrolaVrednostUpdateFormSetOblika01Test(TestCase):


    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        kontrola_vrednost = KontrolaVrednostFactory()
        kontrola_vrednost.save()


    def form_data(self, TF, IF, dn, kv_id, vrednost_check, vrednost_text, vrednost_select ):

        return KontrolaVrednostUpdateFormSetOblika01(
            delovninalog=dn,
            data={
                'form-TOTAL_FORMS': TF,
                'form-INITIAL_FORMS': IF,
                'form-0-id': kv_id,
                'form-0-vrednost_check': vrednost_check,
                'form-0-vrednost_text': vrednost_text,
                'form-0-vrednost_select': vrednost_select,
            }

        )

    def test_valid_data(self):
        kv = KontrolaVrednost.objects.first()
        dn = kv.delovni_nalog
        kv_id = kv.id
        # vrednost check
        form = self.form_data(1, 1, dn, kv_id, True, '', '')
        self.assertTrue(form.is_valid())
