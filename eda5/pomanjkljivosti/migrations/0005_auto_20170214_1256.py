# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0004_auto_20170214_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='datum_ugotovitve',
            new_name='prijava_dne',
        ),
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='prijavil',
            new_name='prijavil_text',
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='prioriteta',
            field=models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')]),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='element_text',
            field=models.CharField(verbose_name='element opisno', blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='etaza_text',
            field=models.CharField(verbose_name='etaža opisno', blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='lokacija_text',
            field=models.CharField(verbose_name='lokacija opisno', blank=True, max_length=255, null=True),
        ),
    ]
