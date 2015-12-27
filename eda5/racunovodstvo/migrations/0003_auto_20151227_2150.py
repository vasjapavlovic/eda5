# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0002_remove_racun_dokument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='delovni_nalog',
            field=models.ForeignKey(null=True, to='delovninalogi.DelovniNalog', blank=True),
        ),
    ]
