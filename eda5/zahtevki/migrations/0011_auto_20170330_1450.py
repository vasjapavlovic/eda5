# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0010_auto_20170214_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_povezava',
            field=models.ManyToManyField(related_name='_zahtevek_povezava_+', blank=True, to='zahtevki.Zahtevek', verbose_name='Povezava zahtevkov'),
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='zahtevek_parent',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Zahtevek Parent', to='zahtevki.Zahtevek'),
        ),
    ]
