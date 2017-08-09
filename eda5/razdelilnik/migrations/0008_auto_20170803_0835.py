# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0007_auto_20170803_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrosekDelitevVrsta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Vrsta delitve stroška',
                'verbose_name_plural': 'Vrsta delitve stroška',
            },
        ),
        migrations.CreateModel(
            name='StrosekKljucDelitve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ključ delitve stroška',
                'verbose_name_plural': 'Ključ delitve stroška',
            },
        ),
        migrations.AlterField(
            model_name='strosekrazdelilnik',
            name='delilnik_kljuc',
            field=models.ForeignKey(blank=True, to='razdelilnik.StrosekKljucDelitve', null=True),
        ),
        migrations.AlterField(
            model_name='strosekrazdelilnik',
            name='delitev_vrsta',
            field=models.ForeignKey(blank=True, to='razdelilnik.StrosekDelitevVrsta', null=True),
        ),
    ]
