# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0010_auto_20151111_1514'),
        ('delovninalogi', '0011_opravilo_is_potrjen'),
    ]

    operations = [
        migrations.AddField(
            model_name='delovninalog',
            name='dokument',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
    ]
