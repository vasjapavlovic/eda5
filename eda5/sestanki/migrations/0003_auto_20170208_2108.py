# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0002_auto_20161105_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sestanek',
            name='sklicatelj',
            field=models.ForeignKey(blank=True, to='partnerji.Partner', null=True),
        ),
    ]
