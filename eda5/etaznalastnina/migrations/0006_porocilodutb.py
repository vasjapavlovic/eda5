# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151215_1854'),
        ('etaznalastnina', '0005_auto_20151216_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='PorociloDutb',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uporabno_dovoljenje', models.BooleanField(default=False)),
                ('stanje_prostora', models.CharField(max_length=255, null=True, blank=True)),
                ('interna', models.OneToOneField(verbose_name='interna LE', to='etaznalastnina.LastniskaEnotaInterna')),
                ('lastnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='lastnik')),
                ('najemnik', models.ForeignKey(null=True, related_name='najemnik', blank=True, to='partnerji.SkupinaPartnerjev')),
                ('placnik', models.ForeignKey(null=True, related_name='placnik', blank=True, to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name': 'poročilo DUTB',
                'verbose_name_plural': 'poročilo DUTB',
            },
        ),
    ]
