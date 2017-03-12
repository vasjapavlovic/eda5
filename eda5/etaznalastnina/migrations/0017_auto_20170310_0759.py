# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0016_auto_20160101_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastniskaenotainterna',
            name='elaborat',
            field=models.ForeignKey(verbose_name='Relacija na Elaborat Etažne Lastnine', to='etaznalastnina.LastniskaEnotaElaborat'),
        ),
    ]
