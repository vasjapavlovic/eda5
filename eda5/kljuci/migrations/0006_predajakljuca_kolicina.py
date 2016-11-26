# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0005_auto_20161126_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='predajakljuca',
            name='kolicina',
            field=models.IntegerField(verbose_name='količina', default=1),
            preserve_default=False,
        ),
    ]
