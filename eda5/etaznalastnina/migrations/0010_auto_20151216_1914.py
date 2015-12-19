# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0009_remove_inernadodatno_v_uporabi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inernadodatno',
            options={'verbose_name': 'dodatek interni LE', 'verbose_name_plural': 'dodatki internim LE'},
        ),
        migrations.AlterField(
            model_name='inernadodatno',
            name='uporabno_dovoljenje',
            field=models.CharField(max_length=22, verbose_name='UporabnoDovoljenje'),
        ),
    ]
