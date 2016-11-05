# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sestanek',
            options={'verbose_name': 'sestanek', 'verbose_name_plural': 'sestanki'},
        ),
        migrations.AlterField(
            model_name='alinejasestanka',
            name='predlagal',
            field=models.ManyToManyField(to='partnerji.Oseba', related_name='predlagal', verbose_name='predlagal', blank=True),
        ),
        migrations.AlterField(
            model_name='alinejasestanka',
            name='proti_predlogu',
            field=models.ManyToManyField(to='partnerji.Oseba', related_name='proti_predlogu', verbose_name='proti predlogu', blank=True),
        ),
    ]
