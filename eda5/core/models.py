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
