# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0002_auto_20171209_2221'),
        ('racunovodstvo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='racun',
            field=models.OneToOneField(null=True, to='racunovodstvo.Racun', blank=True),
        ),
    ]
