# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '__first__'),
        ('delovninalogi', '0002_remove_opravilo_vrsta_stroska'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='vrsta_stroska',
            field=models.ForeignKey(null=True, verbose_name='vrsta stroška', blank=True, to='racunovodstvo.VrstaStroska'),
        ),
    ]
