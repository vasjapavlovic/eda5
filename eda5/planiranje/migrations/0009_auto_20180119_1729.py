# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0008_planaktivnost_zap_st'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plankontrolaspecifikacijaopcijaselect',
            options={'ordering': ['zap_st', 'oznaka']},
        ),
    ]
