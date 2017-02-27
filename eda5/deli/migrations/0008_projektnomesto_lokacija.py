# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacija', '0002_auto_20170226_2340'),
        ('deli', '0007_auto_20170226_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='projektnomesto',
            name='lokacija',
            field=models.ForeignKey(blank=True, verbose_name='Lokacija v Stavbi', to='lokacija.Prostor', null=True),
        ),
    ]
