# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0003_auto_20161124_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajakljucev',
            name='kljuc',
            field=models.ForeignKey(verbose_name='ključ', to='kljuci.Kljuc', default=1),
            preserve_default=False,
        ),
    ]
