# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
        ('delovninalogi', '0012_auto_20180106_1001'),
        ('kontrolnilist', '0006_auto_20180107_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontrolavrednost',
            name='delovni_nalog',
            field=models.ForeignKey(to='delovninalogi.DelovniNalog', default=1, verbose_name='delovni nalog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='kontrola_specifikacija',
            field=models.ForeignKey(to='kontrolnilist.KontrolaSpecifikacija', default=1, verbose_name='specifikacija kontrole'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
            field=models.ForeignKey(to='deli.ProjektnoMesto', default=1, verbose_name='projektno mesto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='vrednost_check',
            field=models.BooleanField(verbose_name='kontrola', default=False),
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='vrednost_select',
            field=models.ForeignKey(to='kontrolnilist.KontrolaSpecifikacijaOpcijaSelect', blank=True, verbose_name='vrednost_select', null=True),
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='vrednost_text',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='vrednost_tekst'),
        ),
    ]
