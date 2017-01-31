# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0011_auto_20170131_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogodek',
            name='poravnava_skode',
            field=models.ForeignKey(null=True, blank=True, related_name='poravnava_skode', to='posta.Dokument'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='prijava_policiji',
            field=models.ForeignKey(null=True, blank=True, related_name='prijava_policiji', to='posta.Dokument'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='prijava_skode',
            field=models.ForeignKey(null=True, blank=True, related_name='prijava_skode', to='posta.Dokument'),
        ),
    ]
