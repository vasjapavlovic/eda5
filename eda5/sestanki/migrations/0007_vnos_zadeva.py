# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0006_auto_20170501_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='vnos',
            name='zadeva',
            field=models.ForeignKey(blank=True, to='sestanki.Zadeva', null=True, verbose_name='točka sestanka'),
        ),
    ]
