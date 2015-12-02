from django.db import models


class PredpisSklop(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna številka")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop predpisov"
        verbose_name_plural = "sklopi predpisov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PredpisPodsklop(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predpis_sklop = models.ForeignKey(PredpisSklop)
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "podsklop predpisov"
        verbose_name_plural = "podsklopi predpisov"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Predpis(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predpis_podsklop = models.ForeignKey(PredpisPodsklop)
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predpis"
        verbose_name_plural = "predpisi"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PredpisOpravilo(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predpis = models.ManyToManyField(Predpis)
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predpis"
        verbose_name_plural = "predpisi"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
