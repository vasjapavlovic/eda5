# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_skupinapartnerjev_oznaka'),
        ('skladisce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='dobavitelj',
            field=models.ForeignKey(default=1, to='partnerji.Partner'),
            preserve_default=False,
        ),
    ]
