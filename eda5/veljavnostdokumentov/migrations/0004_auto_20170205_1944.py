# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veljavnostdokumentov', '0003_auto_20170205_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veljavnostdokumenta',
            name='velja_do',
            field=models.DateField(blank=True, verbose_name='velja do', null=True),
        ),
    ]
