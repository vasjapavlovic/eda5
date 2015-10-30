# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0012_partner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkupinaPartnerjev',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'skupine partnerjev',
                'verbose_name': 'skupina partnerjev',
            },
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'partnerji', 'verbose_name': 'partner'},
        ),
        migrations.AddField(
            model_name='skupinapartnerjev',
            name='partner',
            field=models.ManyToManyField(to='partnerji.Partner'),
        ),
    ]
