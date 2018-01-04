from django.db import models


class OsnovniPodatki(models.Model):

    oznaka = models.CharField(max_length=100, blank=True, null=True)
    oznaka_gen = models.CharField(max_length=100, blank=True, null=True)
    naziv = models.CharField(max_length=255, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class IsActiveModel(models.Model):

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class IsLikvidiranModel(models.Model):

    is_likvidiran = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ZaporednaStevilka(models.Model):

    zap_st = models.IntegerField(default=9999, verbose_name="zaporedna številka")

    class Meta:
        abstract = True


class ObdobjeLeto(models.Model):
    oznaka = models.IntegerField(primary_key=True)


    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        ordering = ('-oznaka',)

    def __str__(self):
        return "%s" % (self.oznaka)


class ObdobjeMesec(models.Model):
    oznaka = models.IntegerField(primary_key=True)
    naziv = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.naziv)


class StatusModel(models.Model):
    draft = 0
    vCakanju = 1
    vPlanu = 2
    vResevanju = 3
    zakljuceno = 4
    deleted = 5
    neaktivno = 6

    STATUS = (
        (draft, 'draft'),
        (vCakanju, 'v čakanju'),
        (vPlanu, 'v planu'),
        (vResevanju, 'v reševanju'),
        (zakljuceno, 'zaključeno'),
        (deleted, 'izbrisano'),
        (neaktivno, 'neaktivno'),
    )

    status = models.IntegerField(default=0, choices=STATUS)

    class Meta:
        abstract = True


class PrioritetaModel(models.Model):
    nizka = 0
    normalna = 1
    velika = 2

    PRIORITETA = (
        (nizka, 'Nizka prioriteta'),
        (normalna, 'Normalna'),
        (velika, 'Velika prioriteta - Nujno'),
    )

    prioriteta = models.IntegerField(default=1, choices=PRIORITETA)

    class Meta:
        abstract = True



class Opombe(models.Model):
    opombe = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


# Kombinacije

class OsnovnaKombinacija(OsnovniPodatki, TimeStampedModel, StatusModel):

        class Meta:
            abstract = True
