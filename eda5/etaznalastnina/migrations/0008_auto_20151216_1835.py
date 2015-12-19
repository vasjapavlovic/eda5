# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151215_1854'),
        ('etaznalastnina', '0007_porocilodutb_v_uporabi'),
    ]

    operations = [
        migrations.CreateModel(
            name='InernaDodatno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('v_uporabi', models.BooleanField(verbose_name='prostor v uporabi', default=False)),
                ('uporabno_dovoljenje', models.BooleanField(default=False)),
                ('stanje_prostora', models.CharField(blank=True, max_length=255, null=True)),
                ('interna', models.OneToOneField(to='etaznalastnina.LastniskaEnotaInterna', verbose_name='interna LE')),
                ('lastnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='lastnik')),
                ('najemnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', blank=True, null=True, related_name='najemnik')),
                ('placnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', blank=True, null=True, related_name='placnik')),
            ],
            options={
                'verbose_name_plural': 'poročilo DUTB',
                'verbose_name': 'poročilo DUTB',
            },
        ),
        migrations.RemoveField(
            model_name='porocilodutb',
            name='interna',
        ),
        migrations.RemoveField(
            model_name='porocilodutb',
            name='lastnik',
        ),
        migrations.RemoveField(
            model_name='porocilodutb',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='porocilodutb',
            name='placnik',
        ),
        migrations.DeleteModel(
            name='PorociloDutb',
        ),
    ]
