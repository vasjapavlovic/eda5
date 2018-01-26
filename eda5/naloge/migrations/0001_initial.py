# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naloga',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('prioriteta', models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(verbose_name='naziv naloge', max_length=255)),
                ('opis', models.TextField(blank=True, null=True, verbose_name='opis naloge')),
                ('rok_izvedbe', models.DateField(verbose_name='rok za izvedbo')),
                ('nosilec', models.ForeignKey(verbose_name='nosilec', to='partnerji.Oseba')),
                ('vnos_sestanka', models.ForeignKey(null=True, verbose_name='sklep sestanka', blank=True, to='sestanki.Vnos')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='Rešuje se pod Zahtevkom', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'naloge',
                'verbose_name': 'naloga',
            },
        ),
    ]
