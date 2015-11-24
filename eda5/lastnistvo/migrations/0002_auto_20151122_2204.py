# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('etaznalastnina', '0002_lastniskaenotaelaborat_posta'),
        ('posta', '0001_initial'),
        ('lastnistvo', '0001_initial'),
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
            field=models.ManyToManyField(verbose_name='lastniška enota', to='etaznalastnina.LastniskaEnotaElaborat'),
        ),
        migrations.AddField(
            model_name='prodaja',
            name='zapisnik_predaje',
            field=models.ForeignKey(verbose_name='zapisnik predaje v posest', to='posta.Dokument'),
        ),
        migrations.AddField(
            model_name='najem',
            name='lastniska_enota',
            field=models.ManyToManyField(verbose_name='lastniška enota', to='etaznalastnina.LastniskaEnotaInterna'),
        ),
        migrations.AddField(
            model_name='najem',
            name='najemna_pogodba',
            field=models.ForeignKey(verbose_name='najemna pogodba', to='posta.Dokument'),
        ),
        migrations.AddField(
            model_name='najem',
            name='najemnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev'),
        ),
    ]
