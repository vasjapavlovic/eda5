from django.db import models

from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel


class IceCreamStore(TimeStampedModel):

    title = models.CharField(max_length=100)
    block_address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("moduli:stores:detail", kwargs={"pk": self.pk})

        return reverse("stores:detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.title