# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0006_auto_20151202_0013'),
        ('planiranje', '0010_auto_20151202_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikelplan',
            name='planirano_opravilo',
            field=models.ForeignKey(blank=True, to='planiranje.PlaniranoOpravilo', null=True),
        ),
    ]
