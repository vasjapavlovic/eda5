# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0001_initial'),
        ('etaznalastnina', '0002_lastniskaenotaelaborat_posta'),
        ('partnerji', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodaja',
            name='kupec',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev'),
        ),
        migrations.AddField(
            model_name='prodaja',
            name='lastniska_enota',
            field=models.ManyToManyField(to='etaznalastnina.LastniskaEnotaElaborat', verbose_name='lastniška enota'),
        ),
        migrations.AddField(
            model_name='prodaja',
            name='zapisnik_predaje',
            field=models.ForeignKey(to='posta.Dokument', verbose_name='zapisnik predaje v posest'),
        ),
        migrations.AddField(
            model_name='najem',
            name='lastniska_enota',
            field=models.ManyToManyField(to='etaznalastnina.LastniskaEnotaInterna', verbose_name='lastniška enota'),
        ),
        migrations.AddField(
            model_name='najem',
            name='najemna_pogodba',
            field=models.ForeignKey(to='posta.Dokument', verbose_name='najemna pogodba'),
        ),
        migrations.AddField(
            model_name='najem',
            name='najemnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev'),
        ),
    ]
