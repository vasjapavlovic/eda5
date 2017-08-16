# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '__first__'),
        ('veljavnostdokumentov', '0002_auto_20170816_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='veljavnostdokumenta',
            name='planirano_opravilo',
            field=models.ForeignKey(blank=True, verbose_name='Planirano Opravilo', null=True, to='planiranje.PlaniranoOpravilo'),
        ),
    ]
