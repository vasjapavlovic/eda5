# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0007_vnos_zadeva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vnos',
            options={'verbose_name': 'vnos sestanka', 'ordering': ['self__oznaka'], 'verbose_name_plural': 'vnosi sestankov'},
        ),
        migrations.AlterField(
            model_name='vnos',
            name='zadeva',
            field=models.ForeignKey(verbose_name='zadeva', null=True, blank=True, to='sestanki.Zadeva'),
        ),
    ]
