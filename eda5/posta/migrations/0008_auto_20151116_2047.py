# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0007_remove_dokument_is_likvidiran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokument',
            name='opis',
        ),
        migrations.AddField(
            model_name='dokument',
            name='naziv',
            field=models.CharField(default='testni dokument', max_length=255, verbose_name='naziv'),
            preserve_default=False,
        ),
    ]
