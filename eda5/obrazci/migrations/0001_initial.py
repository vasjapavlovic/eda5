# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0015_auto_20170209_1601'),
        ('posta', '0023_remove_aktivnost_vrsta_aktivnosti'),
        ('partnerji', '0012_auto_20170302_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObrazecSplosno',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(verbose_name='Oznaka Dokumenta', max_length=100)),
                ('objava', models.DateTimeField(verbose_name='Datum Objave Dokumenta', blank=True, null=True)),
                ('zadeva', models.CharField(verbose_name='Zadeva Dopisa', max_length=255)),
                ('vsebina', models.TextField(verbose_name='Vsebina Dopisa')),
                ('naslovnik', models.ForeignKey(verbose_name='Naslovnik', to='partnerji.Partner', related_name='obrazec_naslovnik')),
                ('oseba_izdelal', models.ForeignKey(verbose_name='Dokument Izdelal', to='partnerji.Oseba', related_name='obrazec_oseba_izdelal')),
                ('oseba_odgovorna', models.ForeignKey(verbose_name='Odgovorna oseba za dokument', to='partnerji.Oseba', related_name='obrazec_oseba_odgovorna')),
                ('posiljatelj', models.ForeignKey(verbose_name='Pošiljatelj', to='partnerji.Partner', related_name='obrazec_posiljatelj')),
                ('priloge', models.ManyToManyField(verbose_name='Priloge', to='arhiv.Arhiviranje')),
                ('vrsta_dokumenta', models.ForeignKey(verbose_name='Vrsta Dokumenta', to='posta.VrstaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'Obrazec Splošno',
            },
        ),
    ]
