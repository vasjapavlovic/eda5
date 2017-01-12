# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0013_arhiviranje_dogodek'),
        ('kljuci', '0009_auto_20170111_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predajakljuca',
            old_name='datum_predaje',
            new_name='predaja_datum',
        ),
        migrations.RenameField(
            model_name='predajakljuca',
            old_name='datum_vracila',
            new_name='vracilo_datum',
        ),
        migrations.RenameField(
            model_name='predajakljuca',
            old_name='opis_vracila',
            new_name='vracilo_posebnosti',
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='predaja_zapisnik',
            field=models.ForeignKey(null=True, related_name='predaja_zapisnik', to='arhiv.Arhiviranje', blank=True),
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='vracilo_zapisnik',
            field=models.ForeignKey(null=True, related_name='vracilo_zapisnik', to='arhiv.Arhiviranje', blank=True),
        ),
    ]
