# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0022_auto_20170208_2108'),
        ('narocila', '0008_auto_20170219_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='narocilodokument',
            name='tip_dokumenta',
        ),
        migrations.AddField(
            model_name='narocilodokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(default=1, verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta'),
            preserve_default=False,
        ),
    ]
