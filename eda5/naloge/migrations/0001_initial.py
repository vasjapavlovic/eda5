# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
        ('zahtevki', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naloga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('prioriteta', models.IntegerField(choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')], default=1)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(verbose_name='naziv naloge', max_length=255)),
                ('opis', models.TextField(verbose_name='opis naloge', null=True, blank=True)),
                ('rok_izvedbe', models.DateField(verbose_name='rok za izvedbo')),
                ('nosilec', models.ForeignKey(verbose_name='nosilec', to='partnerji.Oseba')),
                ('zahtevek', models.ForeignKey(verbose_name='Rešuje se pod Zahtevkom', blank=True, to='zahtevki.Zahtevek', null=True)),
            ],
            options={
                'verbose_name': 'naloga',
                'verbose_name_plural': 'naloge',
            },
        ),
    ]
