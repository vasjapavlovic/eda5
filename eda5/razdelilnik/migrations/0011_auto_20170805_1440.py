# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '__first__'),
        ('razdelilnik', '0010_auto_20170803_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrosekRazdelilnikPostavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('is_strosek_posameznidel', models.NullBooleanField(verbose_name='strosek na posameznem delu')),
                ('delilnik_kljuc', models.ForeignKey(to='razdelilnik.StrosekKljucDelitve', null=True, blank=True)),
                ('delitev_vrsta', models.ForeignKey(to='razdelilnik.StrosekDelitevVrsta', null=True, blank=True)),
                ('lastniska_skupina', models.ForeignKey(to='etaznalastnina.LastniskaSkupina', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'StrosekRazdelilnikPostavka',
                'verbose_name_plural': 'StrosekRazdelilnikPostavke',
            },
        ),
        migrations.RemoveField(
            model_name='strosekrazdelilnik',
            name='delilnik_kljuc',
        ),
        migrations.RemoveField(
            model_name='strosekrazdelilnik',
            name='delitev_vrsta',
        ),
        migrations.RemoveField(
            model_name='strosekrazdelilnik',
            name='is_strosek_posameznidel',
        ),
        migrations.RemoveField(
            model_name='strosekrazdelilnik',
            name='lastniska_skupina',
        ),
        migrations.AddField(
            model_name='strosekrazdelilnikpostavka',
            name='strosek_razdelilnik',
            field=models.ForeignKey(to='razdelilnik.StrosekRazdelilnik'),
        ),
    ]
