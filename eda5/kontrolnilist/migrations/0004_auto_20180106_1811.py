# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0003_auto_20180106_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktivnost',
            name='opravilo',
            field=models.ForeignKey(default=1, verbose_name='opravilo', to='delovninalogi.Opravilo'),
            preserve_default=False,
        ),
    ]
