# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacija', '0004_auto_20170227_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='prostor',
            name='bim_id',
            field=models.CharField(verbose_name='BIM ID', blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='prostor',
            name='etaza',
            field=models.ForeignKey(verbose_name='Etaža', to='lokacija.Etaza'),
        ),
    ]
