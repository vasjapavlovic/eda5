# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naloge', '0002_naloga_sklep_sestanka'),
        ('delovninalogi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='naloga',
            field=models.ManyToManyField(blank=True, to='naloge.Naloga'),
        ),
    ]
