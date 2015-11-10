# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0013_auto_20151030_1310'),
        ('delovninalogi', '0007_remove_opravilo_vrsta_stroska'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='nadzornik',
            field=models.ForeignKey(default=1, to='partnerji.Oseba'),
            preserve_default=False,
        ),
    ]
