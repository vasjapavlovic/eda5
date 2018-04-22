# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0003_auto_20180422_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='klasifikacija_dokumenta',
            field=models.ForeignKey(verbose_name='Klasifikacija dokumenta', to='posta.KlasifikacijaDokumenta', null=True, blank=True),
        ),
    ]
