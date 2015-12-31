# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20151215_1854'),
        ('deli', '0003_auto_20151229_1357'),
        ('partnerji', '0003_auto_20151219_0936'),
        ('planiranje', '0004_auto_20151226_0525'),
        ('delovninalogi', '0004_auto_20151230_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='VzorecOpravila',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField(null=True, blank=True)),
                ('is_potrjen', models.BooleanField(default=False, verbose_name='Potrjeno iz strani nadzornika')),
                ('element', models.ManyToManyField(to='deli.Element')),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo', verbose_name='naročilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('planirano_opravilo', models.ForeignKey(null=True, to='planiranje.PlaniranoOpravilo', blank=True)),
            ],
            options={
                'verbose_name_plural': 'vzorci opravil',
                'verbose_name': 'vzorec opravila',
            },
        ),
    ]
