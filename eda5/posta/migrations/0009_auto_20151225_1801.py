# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_dokument_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokument',
            name='link',
        ),
        migrations.AddField(
            model_name='dokument',
            name='oznaka_baza',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
