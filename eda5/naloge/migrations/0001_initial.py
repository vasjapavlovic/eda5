# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
        ('sestanki', '__first__'),
        ('zahtevki', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naloga',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('prioriteta', models.IntegerField(choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')], default=1)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv naloge')),
                ('opis', models.TextField(null=True, verbose_name='opis naloge', blank=True)),
                ('rok_izvedbe', models.DateField(verbose_name='rok za izvedbo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba', verbose_name='nosilec')),
                ('vnos_sestanka', models.ForeignKey(null=True, to='sestanki.Vnos', verbose_name='sklep sestanka', blank=True)),
                ('zahtevek', models.ForeignKey(null=True, to='zahtevki.Zahtevek', verbose_name='Rešuje se pod Zahtevkom', blank=True)),
            ],
            options={
                'verbose_name': 'naloga',
                'verbose_name_plural': 'naloge',
            },
        ),
    ]
