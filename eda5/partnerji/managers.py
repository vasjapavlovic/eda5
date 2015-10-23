from django.db import models

class OsebaManager(models.Manager):
    def create_oseba(self, priimek=None, ime=None, status=None, kvalifikacije=None, podjetje=None):
        if not podjetje:
            raise ValueError("Izbrati moraš podjetje")

        oseba = self.model(
            priimek = priimek,
            ime = ime,
            status = status,
            kvalifikacije = kvalifikacije,
            podjetje = podjetje,
            )

        oseba.save(using=self._db)
        return oseba
