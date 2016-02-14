# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0005_vzorecopravila'),
    ]

    operations = [
        migrations.AddField(
            model_name='delo',
            name='opis',
            field=models.TextField(null=True, blank=True),
        ),
    ]
