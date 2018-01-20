# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0019_plankontrolaskupina_plan_aktivnost'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontrolaskupina',
            name='aktivnost',
            field=models.ForeignKey(to='kontrolnilist.Aktivnost', verbose_name='aktivnost', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kontrolaskupina',
            name='plan_kontrola_skupina',
            field=models.ForeignKey(to='kontrolnilist.PlanKontrolaSkupina', verbose_name='planiranja skupina kontrol', default=1),
            preserve_default=False,
        ),
    ]
