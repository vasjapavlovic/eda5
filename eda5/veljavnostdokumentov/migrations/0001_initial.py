# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20180104_1543'),
        ('deli', '0002_auto_20180104_1543'),
        ('arhiv', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
        ('planiranje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeljavnostDokumenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('velja_od', models.DateField(verbose_name='velja od', null=True, blank=True)),
                ('velja_do', models.DateField(verbose_name='velja do', null=True, blank=True)),
                ('arhiviranje', models.OneToOneField(verbose_name='arhiviranje', to='arhiv.Arhiviranje')),
                ('narocilo', models.ForeignKey(null=True, blank=True, verbose_name='Narocilo', to='narocila.Narocilo')),
                ('planirano_opravilo', models.ForeignKey(null=True, blank=True, verbose_name='Planirano Opravilo', to='planiranje.PlaniranoOpravilo')),
                ('stavba', models.ForeignKey(null=True, blank=True, verbose_name='stavba', to='deli.Stavba')),
                ('vrsta_stroska', models.ForeignKey(null=True, blank=True, verbose_name='Vrsta Stroška', to='racunovodstvo.VrstaStroska')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
