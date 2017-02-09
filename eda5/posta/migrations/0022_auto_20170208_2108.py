# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0021_auto_20170129_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='avtor',
            field=models.ForeignKey(related_name='avtor', to='partnerji.Partner'),
        ),
        migrations.AlterField(
            model_name='dokument',
            name='naslovnik',
            field=models.ForeignKey(related_name='naslovnik', to='partnerji.Partner'),
        ),
    ]
