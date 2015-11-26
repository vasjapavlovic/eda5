# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151122_2204'),
        ('etaznalastnina', '0002_lastniskaenotaelaborat_posta'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=3)),
                ('datum', models.DateField()),
                ('tip_predaje', models.CharField(verbose_name='ti predaje etažne lastnine', choices=[('A', 'predaja v last'), ('B', 'predaja v najem')], max_length=1)),
                ('trajanje', models.CharField(max_length=50)),
                ('dokument', models.CharField(max_length=50)),
                ('kupec', models.ForeignKey(to='partnerji.Partner', related_name='kupec')),
                ('lastniska_enota_interna', models.ForeignKey(verbose_name='Interna lastniška enota', to='etaznalastnina.LastniskaEnotaInterna')),
                ('prodajalec', models.ForeignKey(to='partnerji.Partner', related_name='prodajalec')),
            ],
            options={
                'verbose_name': 'predaja lastnine',
                'verbose_name_plural': 'predaje lastnine',
            },
        ),
    ]
