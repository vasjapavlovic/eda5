# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151025_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=3)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Država',
                'verbose_name_plural': 'Države',
            },
        ),
        migrations.RemoveField(
            model_name='banka',
            name='oznaka',
        ),
        migrations.AddField(
            model_name='banka',
            name='bancna_oznaka',
            field=models.CharField(default='ab', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banka',
            name='bic_koda',
            field=models.CharField(default='ab', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banka',
            name='naslov',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banka',
            name='drzava',
            field=models.ForeignKey(default=1, to='partnerji.Drzava'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posta',
            name='drzava',
            field=models.ForeignKey(default=1, to='partnerji.Drzava'),
            preserve_default=False,
        ),
    ]
