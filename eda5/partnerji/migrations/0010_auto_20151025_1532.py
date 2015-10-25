# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0009_auto_20151025_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banka',
            name='bancna_oznaka',
            field=models.CharField(max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='banka',
            name='bic_koda',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='drzava',
            name='iso_koda',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='davcna_st',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='maticna_st',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='posta',
            name='postna_stevilka',
            field=models.CharField(max_length=10, unique=True, verbose_name='poštna številka'),
        ),
        migrations.AlterField(
            model_name='trracun',
            name='iban',
            field=models.CharField(max_length=20, unique=True, verbose_name='stevilka računa'),
        ),
    ]
