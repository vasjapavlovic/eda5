# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevcnostanje', '0002_auto_20160122_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delilnik',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='stevec',
            name='oznaka',
            field=models.CharField(unique=True, max_length=13),
        ),
        migrations.AlterUniqueTogether(
            name='odcitek',
            unique_together=set([('delilnik', 'obdobje_leto', 'obdobje_mesec')]),
        ),
    ]
