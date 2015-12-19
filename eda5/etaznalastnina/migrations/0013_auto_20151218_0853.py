# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151215_1854'),
        ('etaznalastnina', '0012_auto_20151216_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternaDodatno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('stanje_prostora', models.CharField(null=True, blank=True, max_length=255)),
                ('interna', models.OneToOneField(verbose_name='interna LE', to='etaznalastnina.LastniskaEnotaInterna')),
                ('lastnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='lastnik')),
                ('najemnik', models.ForeignKey(related_name='najemnik', to='partnerji.SkupinaPartnerjev', blank=True, null=True)),
                ('placnik', models.ForeignKey(related_name='placnik', to='partnerji.SkupinaPartnerjev', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'dodatki internim LE',
                'verbose_name': 'dodatek interni LE',
            },
        ),
        migrations.RemoveField(
            model_name='inernadodatno',
            name='interna',
        ),
        migrations.RemoveField(
            model_name='inernadodatno',
            name='lastnik',
        ),
        migrations.RemoveField(
            model_name='inernadodatno',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='inernadodatno',
            name='placnik',
        ),
        migrations.RemoveField(
            model_name='inernadodatno',
            name='uporabno_dovoljenje',
        ),
        migrations.AlterModelOptions(
            name='uporabnodovoljenje',
            options={'verbose_name_plural': 'uporabna dovoljenja', 'verbose_name': 'uporabno dovoljenje', 'ordering': ['datum']},
        ),
        migrations.DeleteModel(
            name='InernaDodatno',
        ),
        migrations.AddField(
            model_name='internadodatno',
            name='uporabno_dovoljenje',
            field=models.ForeignKey(to='etaznalastnina.UporabnoDovoljenje', blank=True, null=True),
        ),
    ]
