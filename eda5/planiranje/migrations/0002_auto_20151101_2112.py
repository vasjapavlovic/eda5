# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planizdaja',
            name='datum_izdaje',
            field=models.DateField(),
        ),
    ]
