# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrazci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrazecsplosno',
            name='oseba_odgovorna',
            field=models.ForeignKey(blank=True, verbose_name='Odgovorna oseba za dokument', related_name='obrazec_oseba_odgovorna', to='partnerji.Oseba', null=True),
        ),
    ]
