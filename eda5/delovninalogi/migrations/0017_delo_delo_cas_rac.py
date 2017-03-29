# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0016_opravilo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='delo',
            name='delo_cas_rac',
            field=models.DecimalField(max_digits=5, verbose_name='Porabljen čas [UR]', blank=True, decimal_places=2, null=True),
        ),
    ]
