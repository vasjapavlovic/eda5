# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0016_auto_20160107_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktivnost',
            name='vrsta_aktivnosti',
            field=models.IntegerField(choices=[(1, 'Vhodna Pošta'), (2, 'Izhodna Pošta')]),
        ),
    ]
