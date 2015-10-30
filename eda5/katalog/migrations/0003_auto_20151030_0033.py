# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20151030_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelartikla',
            name='dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
    ]
