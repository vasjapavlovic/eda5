# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0011_opravilo_is_potrjen'),
        ('zaznamki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='delovninalog',
            field=models.ForeignKey(null=True, to='delovninalogi.DelovniNalog', blank=True),
        ),
    ]
