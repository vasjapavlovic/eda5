from django.core.urlresolvers import reverse
from django.db import models


# zunanji importi
from eda5.arhiv.models import Arhiviranje
from eda5.core.models import StatusModel
from eda5.partnerji.models import Partner, Oseba
from eda5.posta.models import VrstaDokumenta


class ObrazecSplosno(StatusModel):

	# oznaka dopisa. Se izdela avtomatsko
	# glede na Tip Dopisa, Datumom in Ure objave
	oznaka = models.CharField(
		max_length=100, 
		verbose_name='Oznaka Dokumenta')

	# datum dopisa. Datum se izdela ko se dopis
	# objavi, to je, ko ima status - zaključeno
	datum = models.DateField(
		blank=True, null=True, 
		verbose_name='Datum Objave Dokumenta')

	# polje zadeva v dopisu. Na kratko
	# opišemo o čem bomo pisali
	zadeva = models.CharField(
		max_length=255, 
		verbose_name="Zadeva Dopisa")

	# Vsebina dopisa
	vsebina = models.TextField(
		verbose_name='Vsebina Dopisa')

	# Status dopisa. Ali je Draft ali Zaključeno.
	# pri draft mu številka še ni dodeljena. Ko ga
	# zaključimo se mu avtomatsko dodeli številka.
	# Status se uvozi iz CORE:StatusModel 

	# pošiljatelj. Pošiljatelj je vedno EDAFM. 
	# Želim, da je struktura enaka kot pri
	# pošta:dokument
	posiljatelj = models.ForeignKey(
		Partner, related_name="obrazec_posiljatelj", 
		verbose_name="Pošiljatelj")

	# naslovnik
	naslovnik = models.ForeignKey(
		Partner, related_name="obrazec_naslovnik", 
		verbose_name="Naslovnik")

	# vrsta dokumenta
	vrsta_dokumenta = models.ForeignKey(
		VrstaDokumenta,
		verbose_name='Vrsta Dokumenta')

	# Oseba, ki je dokument izdelala
	oseba_izdelal = models.ForeignKey(
		Oseba, related_name='obrazec_oseba_izdelal', 
		verbose_name='Dokument Izdelal')

	# Odgovorna oseba
	oseba_odgovorna = models.ForeignKey(
		Oseba, related_name='obrazec_oseba_odgovorna',
		verbose_name='Odgovorna oseba za dokument')

	# priloge
	priloge = models.ManyToManyField(
		Arhiviranje,
		verbose_name='Priloge')

	class Meta:
		verbose_name_plural = 'Obrazec Splošno'


	def get_absolute_url(self):
		return reverse('moduli:obrazci:dopis_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return "(%s)%s" % (self.oznaka, self.zadeva)




