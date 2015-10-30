# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20151030_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='model_artikla',
            field=models.ForeignKey(verbose_name='Model', to='katalog.ModelArtikla', default=1),
        ),
    ]
