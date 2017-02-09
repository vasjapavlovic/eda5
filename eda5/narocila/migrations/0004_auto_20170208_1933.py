# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0003_auto_20160117_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(related_name='narocnik', to='partnerji.Partner'),
        ),
    ]
