from django.db import models


class StatusManager(models.Manager):

    ''' ne prikaži objektov s statusom = izbrisano '''
    def not_deleted(self):
        return super(StatusManager, self).get_query_set().exclude(status=5, **kwargs)

    ''' ne prikaži objektov s statusom = zaključeno '''
    def not_closed(self, **kwargs):
        return self.exclude(status=4, **kwargs)

    ''' ne prikaži objektov s statusom = draft '''
    def not_draft(self, **kwargs):
        return self.exclude(status=0, **kwargs)

    ''' ne prikaži objektov s statusom = vcakanju '''
    def not_vcakanju(self, **kwargs):
        return self.exclude(status=1, **kwargs)
