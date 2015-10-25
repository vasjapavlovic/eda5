# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0006_auto_20151025_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='davcni_zavezanec',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
