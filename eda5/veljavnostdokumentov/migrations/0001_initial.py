# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '__first__'),
        ('deli', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
        ('narocila', '0001_initial'),
        ('arhiv', '0004_auto_20171209_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeljavnostDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('velja_od', models.DateField(null=True, verbose_name='velja od', blank=True)),
                ('velja_do', models.DateField(null=True, verbose_name='velja do', blank=True)),
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
