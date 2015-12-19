# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0006_porocilodutb'),
    ]

    operations = [
        migrations.AddField(
            model_name='porocilodutb',
            name='v_uporabi',
            field=models.BooleanField(verbose_name='prostor v uporabi', default=False),
        ),
    ]
