# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0008_auto_20151216_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inernadodatno',
            name='v_uporabi',
        ),
    ]
