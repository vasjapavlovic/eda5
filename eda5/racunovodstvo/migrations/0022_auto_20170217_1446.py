# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0021_remove_racun_opravilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='delovni_nalog',
            field=models.OneToOneField(null=True, blank=True, to='delovninalogi.DelovniNalog'),
        ),
    ]
