# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0003_auto_20151227_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='delilnik_kljuc',
            field=models.CharField(choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')], max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='strosek',
            name='delilnik_vrsta',
            field=models.CharField(choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')], max_length=50, blank=True),
        ),
    ]
