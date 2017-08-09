# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '__first__'),
        ('razdelilnik', '0006_strosekrazdelilnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosekrazdelilnik',
            name='delilnik_kljuc',
            field=models.CharField(max_length=50, blank=True, choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')]),
        ),
        migrations.AddField(
            model_name='strosekrazdelilnik',
            name='delitev_vrsta',
            field=models.CharField(max_length=50, blank=True, choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')]),
        ),
        migrations.AddField(
            model_name='strosekrazdelilnik',
            name='is_strosek_posameznidel',
            field=models.NullBooleanField(verbose_name='strosek na posameznem delu'),
        ),
        migrations.AddField(
            model_name='strosekrazdelilnik',
            name='lastniska_skupina',
            field=models.ForeignKey(to='etaznalastnina.LastniskaSkupina', blank=True, null=True),
        ),
    ]
