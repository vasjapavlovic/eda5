from django.db import models


class StatusManager(models.Manager):

    use_for_related_fields = True

    ''' ne prikaži objektov s statusom = izbrisano '''
    def not_izbrisani(self, **kwargs):
        return self.exclude(status=5, **kwargs)

    ''' ne prikaži objektov s statusom = zaključeno '''
    def not_zakljuceni(self, **kwargs):
        return self.exclude(status=4, **kwargs)


    ''' ne prikaži objektov s statusom = draft '''
    def not_draft(self, **kwargs):
        return self.exclude(status=0, **kwargs)


    ''' ne prikaži objektov s statusom = vcakanju '''
    def not_vcakanju(self, **kwargs):
        return self.exclude(status=1, **kwargs)


    def vsi(self, **kwargs):
        return self.filter()
