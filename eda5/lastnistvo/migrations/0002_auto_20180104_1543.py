# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0001_initial'),
        ('lastnistvo', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('etaznalastnina', '0002_auto_20180104_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodajalastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='predaja_lastnine',
            field=models.ForeignKey(to='lastnistvo.PredajaLastnine'),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='zapisnik_izrocitev',
            field=models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='prodaja_izrocitev_zapisnik'),
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='kupec',
            field=models.ForeignKey(to='partnerji.Partner', related_name='kupec'),
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='prodajalec',
            field=models.ForeignKey(to='partnerji.Partner', related_name='prodajalec'),
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='zahtevek',
            field=models.OneToOneField(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='lastniska_enota',
            field=models.ForeignKey(null=True, blank=True, verbose_name='LE', to='etaznalastnina.LastniskaEnotaInterna'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='najemna_pogodba',
            field=models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='najemna_pogodba'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='predaja_lastnine',
            field=models.ForeignKey(to='lastnistvo.PredajaLastnine'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='vracilo_zapisnik',
            field=models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='najem_vracilo_zapisnik'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='zapisnik_izrocitev',
            field=models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='najem_izrocitev_zapisnik'),
        ),
    ]
