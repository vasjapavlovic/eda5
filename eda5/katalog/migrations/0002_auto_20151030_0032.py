# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelartikla',
            name='dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', null=True, blank=True),
        ),
    ]
