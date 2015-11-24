# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delstavbe',
            name='lastniska_skupina',
            field=models.ForeignKey(null=True, verbose_name='lastniška skupina', to='etaznalastnina.LastniskaSkupina', blank=True),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='podskupina',
            field=models.ForeignKey(to='deli.Podskupina'),
        ),
    ]
