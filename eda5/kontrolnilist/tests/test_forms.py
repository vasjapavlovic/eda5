from django.test import TestCase


from ..forms import AktivnostCreateForm

class TestAktivnostCreateForm(TestCase):


    def setUp(self):
        pass


    def form_data(self, oznaka, naziv, opis):

        return AktivnostCreateForm(
        data={
            'oznaka': oznaka,
            'naziv': naziv,
            'opis': opis,
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
