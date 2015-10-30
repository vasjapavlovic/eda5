# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0012_partner_user'),
        ('etaznalastnina', '0004_auto_20151029_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='naslov',
            field=models.CharField(max_length=255, default='nic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='posta',
            field=models.ForeignKey(default=4, to='partnerji.Posta', verbose_name='pošta'),
            preserve_default=False,
        ),
    ]
