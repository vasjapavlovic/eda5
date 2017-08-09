# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0009_auto_20170803_0849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strosekle',
            old_name='lastniska_enota',
            new_name='lastniska_enota_interna',
        ),
        migrations.RemoveField(
            model_name='strosekle',
            name='strosek',
        ),
        migrations.AddField(
            model_name='strosekle',
            name='strosek_razdelilnik',
            field=models.ForeignKey(default=1, to='razdelilnik.StrosekRazdelilnik'),
            preserve_default=False,
        ),
    ]
