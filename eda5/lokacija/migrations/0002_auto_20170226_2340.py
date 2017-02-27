# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacija', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prostor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, verbose_name='Naziv')),
                ('opis', models.TextField(verbose_name='Opis', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Prostor',
                'verbose_name_plural': 'Prostori',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, verbose_name='Naziv')),
                ('opis', models.TextField(verbose_name='Opis', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Stavba',
                'verbose_name_plural': 'Stavbe',
                'ordering': ['oznaka'],
            },
        ),
        migrations.DeleteModel(
            name='Lokacija',
        ),
        migrations.DeleteModel(
            name='Objekt',
        ),
        migrations.AlterModelOptions(
            name='etaza',
            options={'verbose_name': 'Etaža', 'verbose_name_plural': 'Etaže', 'ordering': ['oznaka']},
        ),
        migrations.AddField(
            model_name='etaza',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='etaza',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='etaza',
            name='naziv',
            field=models.CharField(max_length=255, verbose_name='Naziv', default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etaza',
            name='opis',
            field=models.TextField(verbose_name='Opis', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='etaza',
            name='oznaka',
            field=models.CharField(max_length=20, verbose_name='Oznaka', default='NA', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etaza',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='prostor',
            name='etaza',
            field=models.ForeignKey(to='lokacija.Etaza', verbose_name='Stavba'),
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(default=1, verbose_name='Etaža', to='lokacija.Stavba'),
            preserve_default=False,
        ),
    ]
