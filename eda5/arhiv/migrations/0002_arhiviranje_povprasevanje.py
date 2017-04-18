# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('povprasevanje', '__first__'),
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='povprasevanje',
            field=models.ForeignKey(to='povprasevanje.Povprasevanje', blank=True, null=True),
        ),
    ]
