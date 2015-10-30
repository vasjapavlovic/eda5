# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('etaznalastnina', '0006_auto_20151030_0021'),
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='model_artikla',
            field=models.ForeignKey(verbose_name='Model', to='katalog.ModelArtikla'),
        ),
        migrations.AddField(
            model_name='element',
            name='skupina',
            field=models.ForeignKey(to='deli.Del'),
        ),
        migrations.AddField(
            model_name='del',
            name='lastniska_skupina',
            field=models.ForeignKey(null=True, to='etaznalastnina.LastniskaSkupina', verbose_name='lastniška skupina', blank=True),
        ),
        migrations.AddField(
            model_name='del',
            name='skupina',
            field=models.ForeignKey(to='deli.Podskupina'),
        ),
    ]
