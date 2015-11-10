# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0010_auto_20151110_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='is_potrjen',
            field=models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False),
        ),
    ]
