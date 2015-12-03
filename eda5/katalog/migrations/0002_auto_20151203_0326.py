# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karakteristika',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('enota', models.CharField(blank=True, max_length=20)),
                ('opis', models.CharField(blank=True, max_length=255, verbose_name='opis')),
                ('tip_artikla', models.ForeignKey(blank=True, to='katalog.TipArtikla', null=True)),
            ],
            options={
                'verbose_name_plural': 'karakteristike artiklov',
                'verbose_name': 'karakteristika artikla',
            },
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P1_title',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P1_value',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P2_title',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P2_value',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P3_title',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P3_value',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P4_title',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P4_value',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P5_title',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='P5_value',
        ),
        migrations.RemoveField(
            model_name='obratovalniparameter',
            name='artikel',
        ),
        migrations.AddField(
            model_name='obratovalniparameter',
            name='tip_artikla',
            field=models.ForeignKey(blank=True, to='katalog.TipArtikla', null=True),
        ),
    ]
