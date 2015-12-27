# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0002_remove_racun_dokument'),
        ('arhiv', '0003_auto_20151220_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='racun',
            field=models.ForeignKey(to='racunovodstvo.Racun', null=True, blank=True),
        ),
    ]
