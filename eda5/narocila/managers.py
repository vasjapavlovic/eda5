from django.db import models
from django.utils import timezone


class NarociloManager(models.Manager):

    use_for_related_fields = True

    def veljavna(self, **kwargs):
        return self.filter(datum_veljavnosti__gte=timezone.now(), **kwargs)
