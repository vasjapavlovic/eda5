# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0002_dogodek_pomanjkljivost'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='prijavljena_skoda',
            field=models.TextField(blank=True, null=True, verbose_name='prijavljena škoda'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='st_prijave_skode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Št. prijave škode'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='st_zahtevka_zavarovalnice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Št. zahtevka zavarovalnice'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='st_zavarovalne_police',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Št. zavarovalne police'),
        ),
    ]
