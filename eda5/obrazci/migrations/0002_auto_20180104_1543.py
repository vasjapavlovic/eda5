# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrazci', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obrazecsplosno',
            name='naslovnik',
            field=models.ForeignKey(verbose_name='Naslovnik', to='partnerji.Partner', related_name='obrazec_naslovnik'),
        ),
        migrations.AddField(
            model_name='obrazecsplosno',
            name='oseba_izdelal',
            field=models.ForeignKey(verbose_name='Dokument Izdelal', to='partnerji.Oseba', related_name='obrazec_oseba_izdelal'),
        ),
        migrations.AddField(
            model_name='obrazecsplosno',
            name='oseba_odgovorna',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Odgovorna oseba za dokument', to='partnerji.Oseba', related_name='obrazec_oseba_odgovorna'),
        ),
        migrations.AddField(
            model_name='obrazecsplosno',
            name='posiljatelj',
            field=models.ForeignKey(verbose_name='Pošiljatelj', to='partnerji.Partner', related_name='obrazec_posiljatelj'),
        ),
        migrations.AddField(
            model_name='obrazecsplosno',
            name='priloge',
            field=models.ManyToManyField(verbose_name='Priloge', to='arhiv.Arhiviranje', blank=True),
        ),
        migrations.AddField(
            model_name='obrazecsplosno',
            name='vrsta_dokumenta',
            field=models.ForeignKey(verbose_name='Vrsta Dokumenta', to='posta.VrstaDokumenta'),
        ),
    ]
