# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '__first__'),
        ('racunovodstvo', '0002_remove_racun_stavba'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='stavba',
            field=models.ForeignKey(to='deli.Stavba', blank=True, null=True),
        ),
    ]
