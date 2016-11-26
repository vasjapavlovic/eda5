# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0020_auto_20160214_1947'),
        ('dogodki', '0008_dogodek_prijava_skode'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='poravnava_skode',
            field=models.ForeignKey(related_name='poravnava_skode', blank=True, null=True, to='posta.Dokument'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='prijava_policiji',
            field=models.ForeignKey(related_name='prijava_policiji', blank=True, null=True, to='posta.Dokument'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='prijava_skode',
            field=models.ForeignKey(related_name='prijava_skode', blank=True, null=True, to='posta.Dokument'),
        ),
    ]
