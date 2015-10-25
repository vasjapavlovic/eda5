# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0005_auto_20151025_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='oznaka',
            new_name='davcna_st',
        ),
        migrations.AddField(
            model_name='partner',
            name='is_pravnaoseba',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='maticna_st',
            field=models.CharField(max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='kratko_ime',
            field=models.CharField(max_length=100),
        ),
    ]
