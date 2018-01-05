# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0008_aktivnostparameterspecifikacija'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aktivnostparameterspecifikacija',
            options={'ordering': ['oznaka']},
        ),
        migrations.AddField(
            model_name='aktivnostparameterspecifikacija',
            name='vrsta_vnosa',
            field=models.IntegerField(verbose_name='vrsta vnosa', default=1, choices=[(1, 'check'), (2, 'text'), (3, 'select')]),
        ),
    ]
