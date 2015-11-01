# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0008_auto_20151029_1501'),
        ('delovninalogi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='vrsta_stroska',
            field=models.ForeignKey(to='racunovodstvo.VrstaStroska', verbose_name='vrsta stroška', default=1),
            preserve_default=False,
        ),
    ]
