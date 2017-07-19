# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '__first__'),
        ('razdelilnik', '0003_auto_20170717_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='RacunRazdelilnik',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_razdeljen', models.BooleanField(default=False)),
                ('razdeljen_datum', models.DateField(null=True, blank=True)),
                ('racun', models.OneToOneField(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name': 'RacunRazdelilnik',
                'verbose_name_plural': 'RacunRazdelilnik',
            },
        ),
        migrations.RemoveField(
            model_name='razdelilnikracun',
            name='racun',
        ),
        migrations.RemoveField(
            model_name='razdelilnikracun',
            name='razdelilnik',
        ),
        migrations.AddField(
            model_name='razdelilnik',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')]),
        ),
        migrations.DeleteModel(
            name='RazdelilnikRacun',
        ),
        migrations.AddField(
            model_name='racunrazdelilnik',
            name='razdelilnik',
            field=models.ForeignKey(to='razdelilnik.Razdelilnik'),
        ),
    ]
