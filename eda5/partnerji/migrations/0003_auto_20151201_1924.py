# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151122_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banka',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='banka',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='oseba',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='oseba',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='posta',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posta',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='skupinapartnerjev',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skupinapartnerjev',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='trracun',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='trracun',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
