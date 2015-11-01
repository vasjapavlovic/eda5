from django.db import models


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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



class ObdobjeLeto(models.Model):
    oznaka = models.CharField(max_length=4)
    naziv = models.CharField(max_length=4)

    def __str__(self):
        return "%s" % (self.naziv)


class ObdobjeMesec(models.Model):
    oznaka = models.CharField(max_length=2)
    naziv = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.naziv)


class StatusModel(models.Model):
    draft = 0
    vCakanju = 1
    vPlanu = 2
    vResevanju = 3
    zakljuceno = 4

    STATUS = (
        (draft, 'draft'),
        (vCakanju, 'v čakanju'),
        (vPlanu, 'v planu'),
        (vResevanju, 'v reševanju'),
        (zakljuceno, 'zaključeno'),
        )

    status = models.IntegerField(default=0, choices=STATUS)

    class Meta:
        abstract = True