# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0003_dogodek_cas_dogodka'),
        ('arhiv', '0012_auto_20160117_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='dogodek',
            field=models.ForeignKey(blank=True, null=True, to='dogodki.Dogodek'),
        ),
    ]
