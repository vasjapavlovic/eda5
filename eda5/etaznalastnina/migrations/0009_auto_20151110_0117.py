# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0008_auto_20151030_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastniskaenotainterna',
            name='lastnik',
        ),
        migrations.RemoveField(
            model_name='lastniskaenotainterna',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='lastniskaenotainterna',
            name='placnik',
        ),
        migrations.AlterField(
            model_name='lastniskaskupina',
            name='lastniska_enota',
            field=models.ManyToManyField(blank=True, to='etaznalastnina.LastniskaEnotaElaborat'),
        ),
    ]
