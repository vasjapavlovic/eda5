# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0018_auto_20160120_1914'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dokument',
            unique_together=set([('oznaka', 'avtor', 'vrsta_dokumenta', 'datum_dokumenta')]),
        ),
    ]
