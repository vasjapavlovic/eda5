# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0004_auto_20151215_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zavihek',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=200)),
                ('url_ref', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'verbose_name': 'zavihek',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'zavihki',
            },
        ),
        migrations.RemoveField(
            model_name='modul',
            name='created',
        ),
        migrations.RemoveField(
            model_name='modul',
            name='updated',
        ),
        migrations.AddField(
            model_name='zavihek',
            name='modul',
            field=models.ForeignKey(to='moduli.Modul'),
        ),
    ]
