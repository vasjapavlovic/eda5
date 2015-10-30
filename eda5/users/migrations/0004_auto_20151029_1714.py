# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='partner',
            field=models.ForeignKey(to='partnerji.Partner', blank=True, null=True),
        ),
    ]
