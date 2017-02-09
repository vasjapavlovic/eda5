# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0009_auto_20170112_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_skupina',
            field=models.ManyToManyField(to='partnerji.Partner', related_name='_partner_skupina_+', blank=True),
        ),
    ]
