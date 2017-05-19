# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('arhiv', '0002_arhiviranje_povprasevanje'),
        ('partnerji', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObrazecSplosno',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(verbose_name='Oznaka Dokumenta', max_length=100)),
                ('objava', models.DateTimeField(blank=True, null=True, verbose_name='Datum Objave Dokumenta')),
                ('zadeva', models.CharField(verbose_name='Zadeva Dopisa', max_length=255)),
                ('vsebina', models.TextField(verbose_name='Vsebina Dopisa')),
                ('naslovnik', models.ForeignKey(related_name='obrazec_naslovnik', to='partnerji.Partner', verbose_name='Naslovnik')),
                ('oseba_izdelal', models.ForeignKey(related_name='obrazec_oseba_izdelal', to='partnerji.Oseba', verbose_name='Dokument Izdelal')),
                ('oseba_odgovorna', models.ForeignKey(verbose_name='Odgovorna oseba za dokument', null=True, related_name='obrazec_oseba_odgovorna', blank=True, to='partnerji.Oseba')),
                ('posiljatelj', models.ForeignKey(related_name='obrazec_posiljatelj', to='partnerji.Partner', verbose_name='Pošiljatelj')),
                ('priloge', models.ManyToManyField(verbose_name='Priloge', to='arhiv.Arhiviranje')),
                ('vrsta_dokumenta', models.ForeignKey(verbose_name='Vrsta Dokumenta', to='posta.VrstaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'Obrazec Splošno',
            },
        ),
    ]
