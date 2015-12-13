# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='id_1',
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False),
            preserve_default=False,
        ),
    ]
