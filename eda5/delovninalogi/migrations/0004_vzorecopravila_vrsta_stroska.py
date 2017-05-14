# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '__first__'),
        ('delovninalogi', '0003_opravilo_vrsta_stroska'),
    ]

    operations = [
        migrations.AddField(
            model_name='vzorecopravila',
            name='vrsta_stroska',
            field=models.ForeignKey(verbose_name='vrsta stroška', to='racunovodstvo.VrstaStroska', blank=True, null=True),
        ),
    ]
