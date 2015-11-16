# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivnost',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aktivnost', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
                ('izvajalec', models.ForeignKey(to='partnerji.Oseba', verbose_name='izvajalec poštne storitve')),
            ],
            options={
                'verbose_name': 'poštna storitev',
                'verbose_name_plural': 'poštne storitve',
            },
        ),
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('elektronski', models.BooleanField(verbose_name='elektronski', default=True)),
                ('fizicni', models.BooleanField(verbose_name='elektronski', default=True)),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'arhiv',
                'verbose_name_plural': 'arhiv',
            },
        ),
        migrations.RemoveField(
            model_name='postnastoritev',
            name='dokument',
        ),
        migrations.RemoveField(
            model_name='postnastoritev',
            name='izvajalec',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='posiljatelj',
        ),
        migrations.AddField(
            model_name='dokument',
            name='avtor',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='avtor', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dokument',
            name='naslovnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='naslovnik'),
        ),
        migrations.DeleteModel(
            name='PostnaStoritev',
        ),
        migrations.AddField(
            model_name='arhiv',
            name='dokument',
            field=models.OneToOneField(to='posta.Dokument'),
        ),
        migrations.AddField(
            model_name='dokument',
            name='aktivnost',
            field=models.OneToOneField(to='posta.Aktivnost', default=1),
            preserve_default=False,
        ),
    ]
