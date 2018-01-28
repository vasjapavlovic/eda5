# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolaskupina',
            name='plan_kontrola_skupina',
            field=models.ForeignKey(blank=True, to='planiranje.PlanKontrolaSkupina', null=True, verbose_name='planiranja skupina kontrol'),
        ),
    ]
