# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stevec',
            name='del_stavbe',
            field=models.ForeignKey(null=True, to='deli.DelStavbe', blank=True),
        ),
    ]
