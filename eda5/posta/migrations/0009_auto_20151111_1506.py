# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0013_auto_20151030_1310'),
        ('posta', '0008_auto_20151026_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostnaStoritev',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aktivnost', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'poštne storitve',
                'verbose_name': 'poštna storitev',
            },
        ),
        migrations.AlterModelOptions(
            name='dokument',
            options={'verbose_name_plural': 'dokumenti', 'verbose_name': 'dokument'},
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='datum_prejema',
        ),
        migrations.AddField(
            model_name='dokument',
            name='naslovnik',
            field=models.ForeignKey(to='partnerji.Partner', verbose_name='naslovnik', default=2, related_name='naslovnik'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dokument',
            name='posiljatelj',
            field=models.ForeignKey(to='partnerji.Partner', verbose_name='pošiljatelj', related_name='posiljatelj'),
        ),
        migrations.AddField(
            model_name='postnastoritev',
            name='dokument',
            field=models.OneToOneField(to='posta.Dokument'),
        ),
        migrations.AddField(
            model_name='postnastoritev',
            name='izvajalec',
            field=models.ForeignKey(to='partnerji.Oseba', verbose_name='izvajalec poštne storitve'),
        ),
    ]
