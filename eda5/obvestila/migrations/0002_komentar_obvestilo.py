# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='obvestilo',
            field=models.ForeignKey(to='obvestila.Obvestilo', default=1),
            preserve_default=False,
        ),
    ]
