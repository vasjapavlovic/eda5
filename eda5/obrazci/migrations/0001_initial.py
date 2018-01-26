# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObrazecSplosno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='Oznaka Dokumenta', max_length=100)),
                ('objava', models.DateTimeField(blank=True, null=True, verbose_name='Datum Objave Dokumenta')),
                ('zadeva', models.CharField(verbose_name='Zadeva Dopisa', max_length=255)),
                ('vsebina', models.TextField(verbose_name='Vsebina Dopisa')),
                ('naslovnik', models.ForeignKey(related_name='obrazec_naslovnik', verbose_name='Naslovnik', to='partnerji.Partner')),
                ('oseba_izdelal', models.ForeignKey(related_name='obrazec_oseba_izdelal', verbose_name='Dokument Izdelal', to='partnerji.Oseba')),
                ('oseba_odgovorna', models.ForeignKey(related_name='obrazec_oseba_odgovorna', null=True, verbose_name='Odgovorna oseba za dokument', blank=True, to='partnerji.Oseba')),
                ('posiljatelj', models.ForeignKey(related_name='obrazec_posiljatelj', verbose_name='Pošiljatelj', to='partnerji.Partner')),
                ('priloge', models.ManyToManyField(blank=True, to='arhiv.Arhiviranje', verbose_name='Priloge')),
                ('vrsta_dokumenta', models.ForeignKey(verbose_name='Vrsta Dokumenta', to='posta.VrstaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'Obrazec Splošno',
            },
        ),
    ]
