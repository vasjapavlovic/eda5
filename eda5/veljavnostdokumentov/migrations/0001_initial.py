# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('narocila', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeljavnostDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('velja_od', models.DateField(blank=True, null=True, verbose_name='velja od')),
                ('velja_do', models.DateField(blank=True, null=True, verbose_name='velja do')),
                ('arhiviranje', models.OneToOneField(verbose_name='arhiviranje', to='arhiv.Arhiviranje')),
                ('narocilo', models.ForeignKey(null=True, verbose_name='Narocilo', blank=True, to='narocila.Narocilo')),
                ('planirano_opravilo', models.ForeignKey(null=True, verbose_name='Planirano Opravilo', blank=True, to='planiranje.PlaniranoOpravilo')),
                ('stavba', models.ForeignKey(null=True, verbose_name='stavba', blank=True, to='deli.Stavba')),
                ('vrsta_stroska', models.ForeignKey(null=True, verbose_name='Vrsta Stroška', blank=True, to='racunovodstvo.VrstaStroska')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
