# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NastavitevPartnerja',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('partner', models.OneToOneField(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'nastavitve',
                'verbose_name': 'nastavitev',
            },
        ),
    ]
