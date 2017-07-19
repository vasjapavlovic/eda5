# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '__first__'),
        ('deli', '__first__'),
        ('core', '__first__'),
        ('razdelilnik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Razdelilnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('stavba', models.ForeignKey(to='deli.Stavba')),
            ],
            options={
                'verbose_name': 'Razdelilnik',
                'verbose_name_plural': 'Razdelilniki',
            },
        ),
        migrations.CreateModel(
            name='RazdelilnikRacun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('is_razdeljen', models.BooleanField(default=False)),
                ('razdeljen_datum', models.DateField(null=True, blank=True)),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
                ('razdelilnik', models.ForeignKey(to='razdelilnik.Razdelilnik')),
            ],
            options={
                'verbose_name': 'RazdelilnikRacun',
                'verbose_name_plural': 'RazdelilnikRacun',
            },
        ),
    ]
