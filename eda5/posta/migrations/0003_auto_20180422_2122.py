# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0002_klasifikacijadokumenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasifikacijadokumenta',
            name='postopek_oznaka',
            field=models.CharField(verbose_name='Oznaka postopka', max_length=10),
        ),
        migrations.AlterField(
            model_name='klasifikacijadokumenta',
            name='proces_oznaka',
            field=models.CharField(verbose_name='Oznaka procesa', max_length=10),
        ),
    ]
