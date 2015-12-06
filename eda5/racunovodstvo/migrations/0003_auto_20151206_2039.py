# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0002_auto_20151206_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racun',
            name='dokument',
            field=models.ForeignKey(null=True, to='posta.Dokument', blank=True),
        ),
    ]
