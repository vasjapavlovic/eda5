from django.db import models
from django.core.urlresolvers import reverse

# Managers
from . import managers

# Models
from eda5.core.models import TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel
from eda5.delovninalogi.models import DelovniNalog
from eda5.partnerji.models import Partner
from eda5.zahtevki.models import Zahtevek


class Reklamacija(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel):

	''' 
	V modulu Reklamacije se beležijo reklamacije računov, izvedbe del,
	reklamacije materiala. Sledenje reklamacijam so v primeru EDAFM
	tudi merljiv cilj po ISO 9001.

	'''
	#=================================================
	# ATRIBTUI
	#-------------------------------------------------

	#=================================================
	# osnovni podatki reklamacije
	#-------------------------------------------------
	# oznaka, oznaka reklamacije. Oblika Leto+zap.št.
	# naziv, kratko ime reklamacije
	# opis, daljši opis vsebine reklamacije
	# datum, kdaj se je reklamacija vložila
	# narocnik, reklamira blago ali storitev
	# izvajalec, se mu reklamira blago ali storitev
	# status
	# okvirni_strosek, evidenca ISO 9001

	#=================================================
	# relacije z zahtevki, delovni nalogi,
	#-------------------------------------------------
	# zahtevek, reklamacija je del zahtevka
	# delovninalog, reklamira se delovni nalog


	oznaka = models.CharField(
		max_length=255,
		verbose_name="oznaka",)
 
	naziv = models.CharField(
		max_length=255,
		verbose_name="naziv",)

	opis = models.TextField(
		verbose_name="opis",)

	datum = models.DateField(
		verbose_name="datum vložene reklamacije",)

	narocnik = models.ForeignKey(
		Partner,
		related_name="reklamacija_narocnik",
		verbose_name="naročnik",)
 
	izvajalec = models.ForeignKey(
		Partner,
		related_name="reklamacija_izvajalec",
		verbose_name="izvajalec",)

	okvirni_strosek = models.DecimalField(
		# 99999,99
		max_digits=7,
		decimal_places=2,
		verbose_name="Okvirni Strošek Reklamacije",)

	zahtevek = models.ForeignKey( 
		Zahtevek,
		blank=True, null=True,
		verbose_name="zahtevek")
	
	delovninalog = models.ForeignKey( 
		DelovniNalog,
		blank=True, null=True,
		verbose_name="delovninalog")
		# naprej se dodajo še reklamacije materiala ...


	#---------------------------------------------------------
	# OBJECT MANAGER
	# ========================================================
	objects = managers.ReklamacijaManager()

	def get_absolute_url(self):
		return reverse('moduli:reklamacije:reklamacija_detail', kwargs={'pk': self.pk})

	#---------------------------------------------------------
	# META and STR
	# ========================================================
	class Meta:
		verbose_name_plural = "Reklamacije"

	def __str__(self):
		return "%s | %s | %s" % (self.oznaka, self.datum, self.naziv)


