# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0004_auto_20151216_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lastniskaenotaelaborat',
            options={'ordering': ('id',), 'verbose_name': 'lastniška enota elaborat', 'verbose_name_plural': 'lastniške enote elaborat'},
        ),
        migrations.AlterField(
            model_name='lastniskaenotaelaborat',
            name='oznaka',
            field=models.CharField(unique=True, max_length=4, verbose_name='številka dela stavbe'),
        ),
        migrations.AlterField(
            model_name='lastniskaenotainterna',
            name='oznaka',
            field=models.CharField(unique=True, max_length=5, verbose_name='interna številka dela stavbe'),
        ),
        migrations.AlterField(
            model_name='lastniskaskupina',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='program',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
