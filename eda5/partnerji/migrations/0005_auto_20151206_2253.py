# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20151206_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='skupina_partnerjev',
        ),
        migrations.AddField(
            model_name='skupinapartnerjev',
            name='partner',
            field=models.ManyToManyField(to='partnerji.Partner'),
        ),
    ]
