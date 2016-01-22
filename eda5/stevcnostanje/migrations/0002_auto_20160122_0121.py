# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_auto_20151229_1357'),
        ('stevcnostanje', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stevec',
            name='del_stavbe',
        ),
        migrations.AddField(
            model_name='stevec',
            name='projektno_mesto',
            field=models.ForeignKey(blank=True, null=True, to='deli.ProjektnoMesto'),
        ),
    ]
