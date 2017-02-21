# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0008_auto_20170220_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='prijava_dne',
            new_name='ugotovljeno_dne',
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='opis',
            field=models.TextField(verbose_name='opis pomanjkljivosti', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='opis_text',
            field=models.TextField(verbose_name='Problem', default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='element',
            field=models.ForeignKey(to='deli.ProjektnoMesto', verbose_name='element', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='naziv',
            field=models.CharField(verbose_name='naziv pomanjkljivosti', max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', verbose_name='zahtevek', null=True, blank=True),
        ),
    ]
