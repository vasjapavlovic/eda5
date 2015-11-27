# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('deli', '0002_auto_20151122_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjektnoMesto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(max_length=255)),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('tip_elementa', models.ForeignKey(to='katalog.TipArtikla')),
            ],
            options={
                'verbose_name': 'projektno mesto',
                'verbose_name_plural': 'projektna mesta',
            },
        ),
        migrations.RemoveField(
            model_name='element',
            name='datum_prevzema_v_upravljanje',
        ),
        migrations.RemoveField(
            model_name='element',
            name='del_stavbe',
        ),
        migrations.RemoveField(
            model_name='element',
            name='dokumentacija',
        ),
        migrations.AddField(
            model_name='element',
            name='projektno_mesto',
            field=models.ForeignKey(default=1, to='deli.ProjektnoMesto'),
            preserve_default=False,
        ),
    ]
