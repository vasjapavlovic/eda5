# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0009_auto_20161126_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogodek',
            name='poravnava_skode',
            field=models.OneToOneField(null=True, to='posta.Dokument', blank=True, related_name='poravnava_skode'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='prijava_policiji',
            field=models.OneToOneField(null=True, to='posta.Dokument', blank=True, related_name='prijava_policiji'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='prijava_skode',
            field=models.OneToOneField(null=True, to='posta.Dokument', blank=True, related_name='prijava_skode'),
        ),
    ]
