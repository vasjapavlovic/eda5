# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20160105_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='NastavitevPartnerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('partner', models.OneToOneField(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'nastavitve',
                'verbose_name': 'nastavitev',
            },
        ),
    ]
