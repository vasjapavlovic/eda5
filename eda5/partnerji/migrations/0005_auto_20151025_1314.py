# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20151025_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banka',
            name='drzava',
        ),
        migrations.AddField(
            model_name='banka',
            name='posta',
            field=models.ForeignKey(default=1, to='partnerji.Posta'),
            preserve_default=False,
        ),
    ]
