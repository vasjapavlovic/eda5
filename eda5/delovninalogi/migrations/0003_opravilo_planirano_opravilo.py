# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0002_auto_20151226_0214'),
        ('delovninalogi', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='planirano_opravilo',
            field=models.ForeignKey(to='planiranje.PlaniranoOpravilo', null=True, blank=True),
        ),
    ]
