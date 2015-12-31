# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0012_auto_20151231_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modul',
            options={'verbose_name_plural': 'moduli', 'verbose_name': 'modul', 'ordering': ['naziv']},
        ),
        migrations.AlterModelOptions(
            name='zavihek',
            options={'verbose_name_plural': 'zavihki', 'verbose_name': 'zavihek', 'ordering': ['oznaka']},
        ),
        migrations.RemoveField(
            model_name='modul',
            name='zap_st',
        ),
        migrations.RemoveField(
            model_name='zavihek',
            name='zap_st',
        ),
    ]
