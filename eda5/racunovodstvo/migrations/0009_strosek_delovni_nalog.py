# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0007_remove_opravilo_vrsta_stroska'),
        ('racunovodstvo', '0008_auto_20151029_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosek',
            name='delovni_nalog',
            field=models.OneToOneField(blank=True, null=True, to='delovninalogi.DelovniNalog'),
        ),
    ]
