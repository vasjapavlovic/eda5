# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0012_auto_20170218_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delovninalog',
            name='nosilec',
            field=models.ForeignKey(null=True, to='partnerji.Oseba', blank=True, verbose_name='Izvajalec (kdo bo delo izvedel)'),
        ),
    ]
