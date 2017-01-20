# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0013_arhiviranje_dogodek'),
        ('lastnistvo', '0017_auto_20170113_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='najemlastnine',
            name='zapisnik_izrocitev',
            field=models.ForeignKey(related_name='najem_izrocitev_zapisnik', blank=True, null=True, to='arhiv.Arhiviranje'),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='zapisnik_izrocitev',
            field=models.ForeignKey(related_name='prodaja_izrocitev_zapisnik', blank=True, null=True, to='arhiv.Arhiviranje'),
        ),
        migrations.AlterField(
            model_name='najemlastnine',
            name='vracilo_zapisnik',
            field=models.ForeignKey(related_name='najem_vracilo_zapisnik', blank=True, null=True, to='arhiv.Arhiviranje'),
        ),
    ]
