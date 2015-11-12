# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delovninalog',
            name='nosilec',
            field=models.ForeignKey(to='partnerji.Oseba', null=True, blank=True),
        ),
    ]
