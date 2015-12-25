# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0006_auto_20151216_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='parent_modul',
            field=models.ForeignKey(to='moduli.Modul', blank=True, null=True),
        ),
    ]
