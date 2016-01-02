# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predaja_lastnine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predajadaljinca',
            name='daljinec',
        ),
        migrations.RemoveField(
            model_name='predajadaljinca',
            name='predaja_lastnine',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='daljinec',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='kupec',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='lastniska_enota_interna',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='prodajalec',
        ),
        migrations.DeleteModel(
            name='Daljinec',
        ),
        migrations.DeleteModel(
            name='PredajaDaljinca',
        ),
        migrations.DeleteModel(
            name='PredajaLastnine',
        ),
    ]
