# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0009_strosek_delovni_nalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='lastniska_skupina',
            field=models.ForeignKey(to='etaznalastnina.LastniskaSkupina'),
        ),
    ]
