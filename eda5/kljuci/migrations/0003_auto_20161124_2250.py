# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0002_auto_20160110_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sklopkljucev',
            name='element',
        ),
        migrations.RemoveField(
            model_name='predajakljucev',
            name='kljuc',
        ),
        migrations.AddField(
            model_name='predajakljucev',
            name='kljuc',
            field=models.ForeignKey(null=True, to='kljuci.Kljuc', blank=True),
        ),
    ]
