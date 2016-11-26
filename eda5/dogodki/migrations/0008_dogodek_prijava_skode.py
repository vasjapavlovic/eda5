# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0020_auto_20160214_1947'),
        ('dogodki', '0007_auto_20161103_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='prijava_skode',
            field=models.ForeignKey(to='posta.Dokument', null=True, blank=True),
        ),
    ]
