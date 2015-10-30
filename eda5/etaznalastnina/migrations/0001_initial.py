# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0011_auto_20151025_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtaznaLastninaElaborat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(verbose_name='številka dela stavbe', max_length=4)),
                ('povrsina_tlorisna_neto', models.CharField(verbose_name='neto tlorisna površina', max_length=4)),
            ],
            options={
                'verbose_name_plural': 'etažna lastnina elaborat',
                'verbose_name': 'etažna lastnina elaborat',
            },
        ),
        migrations.CreateModel(
            name='EtaznaLastninaInterna',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(verbose_name='interna številka dela stavbe', max_length=4)),
                ('povrsina_tlorisna_neto', models.CharField(verbose_name='neto tlorisna površina', max_length=4)),
                ('elaborat', models.ForeignKey(to='etaznalastnina.EtaznaLastninaElaborat')),
                ('lastnik', models.ForeignKey(to='partnerji.Partner', related_name='lastnik')),
                ('najemnik', models.ForeignKey(to='partnerji.Partner', null=True, related_name='najemnik', blank=True)),
                ('placnik', models.ForeignKey(to='partnerji.Partner', related_name='placnik')),
            ],
            options={
                'verbose_name_plural': 'etažna lastnina interna',
                'verbose_name': 'etažna lastnina interna',
            },
        ),
    ]
