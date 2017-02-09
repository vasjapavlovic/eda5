# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0021_auto_20170129_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='najemlastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='kupec',
            field=models.ForeignKey(related_name='kupec', to='partnerji.Partner'),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='prodajalec',
            field=models.ForeignKey(related_name='prodajalec', to='partnerji.Partner'),
        ),
        migrations.AlterField(
            model_name='prodajalastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
    ]
