# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0008_auto_20151225_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modul',
            name='parent',
        ),
        migrations.AddField(
            model_name='zavihek',
            name='parent',
            field=models.ForeignKey(blank=True, to='moduli.Zavihek', null=True),
        ),
    ]
