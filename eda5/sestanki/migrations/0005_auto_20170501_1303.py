# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0004_auto_20170501_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpombaVnosa',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('opomnil', models.CharField(max_length=255, verbose_name='opomnil', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'opomba vnosa',
                'verbose_name_plural': 'opombe vnosov',
            },
        ),
        migrations.CreateModel(
            name='Vnos',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('izvede', models.CharField(max_length=255, verbose_name='izvede/realizira', blank=True, null=True)),
                ('rok_izvedbe', models.DateField(verbose_name='rok izvedbe', blank=True, null=True)),
                ('rok_izvedbe_opis', models.CharField(max_length=255, verbose_name='rok izvedbe opisno', blank=True, null=True)),
                ('dopolnitev_vnosov', models.ManyToManyField(verbose_name='dopolnitev vnosov', blank=True, to='sestanki.Vnos', related_name='_dopolnitev_vnosov_+')),
                ('tocka', models.ForeignKey(verbose_name='točka sestanka', to='sestanki.Tocka')),
            ],
            options={
                'verbose_name': 'vnos sestanka',
                'verbose_name_plural': 'vnos sestankov',
            },
        ),
        migrations.RemoveField(
            model_name='opombasklepa',
            name='sklep',
        ),
        migrations.RemoveField(
            model_name='sklep',
            name='dopolnitev_sklepov',
        ),
        migrations.RemoveField(
            model_name='sklep',
            name='tocka',
        ),
        migrations.DeleteModel(
            name='OpombaSklepa',
        ),
        migrations.DeleteModel(
            name='Sklep',
        ),
        migrations.AddField(
            model_name='opombavnosa',
            name='vnos',
            field=models.ForeignKey(verbose_name='vnos sestanka', to='sestanki.Vnos'),
        ),
    ]
