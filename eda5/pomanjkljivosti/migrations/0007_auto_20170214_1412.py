# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0006_pomanjkljivost_zahtevek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='naziv',
            field=models.TextField(verbose_name='Problem'),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='prijava_dne',
            field=models.DateField(verbose_name='prijava dne'),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='prijavil_text',
            field=models.CharField(verbose_name='prijavil', max_length=255),
        ),
    ]
