# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0011_auto_20170129_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='kljuc',
            name='opomba_statusa_kljuca',
            field=models.CharField(blank=True, null=True, max_length=255, verbose_name='opomba spremembe statusa ključa'),
        ),
    ]
