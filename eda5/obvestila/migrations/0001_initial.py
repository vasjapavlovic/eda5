# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('vsebina', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'komentarji',
                'verbose_name': 'komentar',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Obvestilo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('onaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('vsebina', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'obvestila',
                'verbose_name': 'obvestilo',
                'ordering': ['-created'],
            },
        ),
    ]
