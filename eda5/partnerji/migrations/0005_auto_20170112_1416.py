# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20160105_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='is_skupina_partnerjev',
            field=models.NullBooleanField(verbose_name='Skupina partnerjev?', default=False),
        ),
        migrations.AddField(
            model_name='partner',
            name='opis_skupine_partnerjev',
            field=models.CharField(null=True, blank=True, verbose_name='opis skupine partnerjev', max_length=255),
        ),
        migrations.AddField(
            model_name='partner',
            name='skupina_partnerja',
            field=models.ManyToManyField(to='partnerji.Partner', blank=True, related_name='_skupina_partnerja_+'),
        ),
    ]
