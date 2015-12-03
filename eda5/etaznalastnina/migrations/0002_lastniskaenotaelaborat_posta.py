# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='posta',
            field=models.ForeignKey(to='partnerji.Posta', verbose_name='pošta'),
        ),
    ]
