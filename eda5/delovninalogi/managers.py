from django.db import models
from django.db.models import Q




class OpraviloManager(models.Manager):

    def create_opravilo(self,
                        oznaka=None,
                        naziv=None,
                        rok_izvedbe=None,
                        narocilo=None,
                        zahtevek=None,
                        ):
        if not zahtevek:
            raise ValueError("Izbran mora biti zahtevek")

        opravilo = self.model(oznaka=oznaka,
                              naziv=naziv,
                              rok_izvedbe=rok_izvedbe,
                              narocilo=narocilo,
                              # element=element,
                              zahtevek=zahtevek,
                              )

        opravilo.save(using=self._db)
        return opravilo

class DelovniNalogManager(models.Manager):

  use_for_related_fields = True


  # nepopolno izpolnjeni delovni nalogi
  def dn_draft(self, **kwargs):
      return self.filter(status=0)


  # delovni nalogi v čakanju
  def dn_vcakanju(self, **kwargs):
      return self.filter(status=1)


  # delovni nalogi v planu
  def dn_vplanu(self, **kwargs):
      return self.filter(status=2)


  # delovni nalogi v reševanju
  def dn_vresevanju(self, **kwargs):
    return self.filter(status=3)



  # zaključeni delovni nalogi
  def dn_zakljuceni(self, **kwargs):
      return self.filter(status=4).order_by("opravilo__is_potrjen", "-datum_stop")

      '''
      razvrstitev:
      -nepotrjeni naprej
      -zadnje končani naprej
      '''





