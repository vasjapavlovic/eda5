# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0003_remove_delovninalog_dokument'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeloVrsta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('stopnja_ddv', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
            options={
                'verbose_name': 'vrsta dela',
                'verbose_name_plural': 'vrste del',
            },
        ),
        migrations.CreateModel(
            name='DeloVrstaSklop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name': 'sklop vrst del',
                'verbose_name_plural': 'sklopi vrst del',
            },
        ),
        migrations.AddField(
            model_name='delovrsta',
            name='sklo',
            field=models.ForeignKey(to='delovninalogi.DeloVrstaSklop'),
        ),
        migrations.AddField(
            model_name='delo',
            name='vrsta_dela',
            field=models.ForeignKey(to='delovninalogi.DeloVrsta', null=True, blank=True),
            preserve_default=False,
        ),
    ]
