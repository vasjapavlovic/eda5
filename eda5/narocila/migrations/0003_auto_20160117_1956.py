# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='NarociloDokument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('tip_dokumenta', models.IntegerField(choices=[(1, 'e-pošta'), (2, 'naročilnica'), (3, 'pogodba')])),
            ],
            options={
                'verbose_name_plural': 'naročilo z dokumentom',
                'verbose_name': 'naročilo z dokumentom',
            },
        ),
        migrations.RemoveField(
            model_name='narocilo',
            name='narocilo_pogodba',
        ),
        migrations.DeleteModel(
            name='NarociloPogodba',
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_dokument',
            field=models.OneToOneField(blank=True, null=True, to='narocila.NarociloDokument'),
        ),
    ]
