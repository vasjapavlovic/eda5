# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KontrolaSpecifikacija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=100, blank=True, null=True)),
                ('oznaka_gen', models.CharField(max_length=100, blank=True, null=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrsta_vnosa', models.IntegerField(default=1, verbose_name='vrsta vnosa', choices=[(1, 'check'), (2, 'text'), (3, 'select')])),
                ('aktivnost', models.ForeignKey(verbose_name='aktivnost', to='kontrolnilist.Aktivnost')),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
        migrations.RemoveField(
            model_name='aktivnostparameterspecifikacija',
            name='aktivnost',
        ),
        migrations.RemoveField(
            model_name='opcijaselect',
            name='aktivnost_parameter_specifikacija',
        ),
        migrations.DeleteModel(
            name='AktivnostParameterSpecifikacija',
        ),
        migrations.AddField(
            model_name='opcijaselect',
            name='kontrola_specifikacija',
            field=models.ForeignKey(to='kontrolnilist.KontrolaSpecifikacija', default=1, verbose_name='specifikacija kontrole'),
            preserve_default=False,
        ),
    ]
