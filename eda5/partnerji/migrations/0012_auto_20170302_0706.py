# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0011_auto_20170301_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='davcni_zavezanec',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='partner',
            name='is_pravnaoseba',
            field=models.NullBooleanField(),
        ),
    ]
