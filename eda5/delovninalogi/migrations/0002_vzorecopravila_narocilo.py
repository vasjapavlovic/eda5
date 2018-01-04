# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vzorecopravila',
            name='narocilo',
            field=models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo'),
        ),
    ]
