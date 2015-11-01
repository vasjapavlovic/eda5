# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0005_narocilopogodba_predmet_pogodbe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='narocilo',
            options={'verbose_name_plural': 'naročila', 'verbose_name': 'naročilo'},
        ),
        migrations.AlterField(
            model_name='narocilo',
            name='oznaka',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='narocilo',
            name='predmet',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='narocilopogodba',
            name='predmet_pogodbe',
            field=models.CharField(max_length=255, verbose_name='številka pogodbe'),
        ),
    ]
