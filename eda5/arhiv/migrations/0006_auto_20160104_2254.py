# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0005_auto_20151228_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiviranje',
            name='racun',
            field=models.OneToOneField(null=True, blank=True, to='racunovodstvo.Racun'),
        ),
    ]
