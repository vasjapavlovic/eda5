# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predpis',
            name='predpis_podsklop',
        ),
        migrations.AddField(
            model_name='predpisopravilo',
            name='predpis_podsklop',
            field=models.ForeignKey(blank=True, null=True, to='predpisi.PredpisPodsklop'),
        ),
        migrations.AlterField(
            model_name='predpisopravilo',
            name='predpis',
            field=models.ManyToManyField(blank=True, to='predpisi.Predpis'),
        ),
        migrations.AlterField(
            model_name='predpispodsklop',
            name='predpis_sklop',
            field=models.ForeignKey(blank=True, null=True, to='predpisi.PredpisSklop'),
        ),
    ]
