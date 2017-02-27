# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacija', '0003_auto_20170226_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etaza',
            name='oznaka',
            field=models.CharField(max_length=50, verbose_name='Oznaka', unique=True),
        ),
        migrations.AlterField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(verbose_name='Stavba', to='lokacija.Stavba'),
        ),
    ]
