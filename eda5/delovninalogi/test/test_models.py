from test_plus.test import TestCase
from ..models import Opravilo

from eda5.zahtevki.models import Zahtevek


class TestOpravilo(TestCase):

    def setUp(self):

        oznaka = 'OPR-2015-1'
        predmet = 'TestniZahtevek'
        rok_izvedbe = '2015-11-15'
        nosilec = 1
        narocilo = 1

        

        Zahtevek.objects.create(oznaka=oznaka,
                                predmet=predmet,
                                rok_izvedbe=rok_izvedbe,
                                narocilo=narocilo,
                                nadzornik=nadzornik,
                              )


        zahtevek = 1
        narocilo = 1
        nadzornik = 1
        oznaka = 'OPR-2015-1'
        naziv = 'TestnoOpravilo'
        rok_izvedbe = '2015-11-15'

        Opravilo.objects.create(oznaka=oznaka,
                                naziv=naziv,
                                rok_izvedbe=rok_izvedbe,
                                narocilo=narocilo,
                                # element=element,
                                zahtevek=zahtevek,
                                nadzornik=nadzornik,
                              )

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "OPR-2015-1 - TestnoOpravilo"  # This is the default username for self.make_user()
        )


# class Opravilo(TimeStampedModel, IsActiveModel):
#     # ---------------------------------------------------------------------------------------
#     # ATRIBUTES
#     #   Relations
#     zahtevek = models.ForeignKey(Zahtevek)
#     narocilo = models.ForeignKey(Narocilo, verbose_name='naročilo')
#     nadzornik = models.ForeignKey(Oseba)
#     '''pod naročilo je odzadaj tudi relacija na naročnika in izvajalca'''
#     # planirano_opravilo = models.ForeignKey(PlanOpravilo, blank=True, null=True)
#     element = models.ManyToManyField(Element)
#     #   Mandatory
#     oznaka = models.CharField(max_length=20)
#     naziv = models.CharField(max_length=255)
#     rok_izvedbe = models.DateField()
#     is_potrjen = models.BooleanField(default=False, verbose_name="Potrjeno iz strani nadzornika")
#     #   Optional


#     # OBJECT MANAGER
#     objects = managers.OpraviloManager()

#     # CUSTOM PROPERTIES

#     @property
#     def delovninalog_koncan_sorted_by_date(self):
#         return self.delovninalog_set.exclude(datum_stop__isnull=True).order_by("datum_start")

#     @property
#     def delovninalog_vdelu_sorted_by_date(self):
#         return self.delovninalog_set.exclude(datum_stop__isnull=False).order_by("datum_start")

#     # METHODS
#     def get_absolute_url(self):
#         return reverse("moduli:delovninalogi:opravilo_detail", kwargs={'pk': self.pk})

#     # META AND STRING
#     class Meta:
#         verbose_name = "Opravilo"
#         verbose_name_plural = "Opravila"

#     def __str__(self):
#         return "%s - %s" % (self.oznaka, self.naziv)
