# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20151030_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narocilo',
            name='dodatna_dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
    ]
