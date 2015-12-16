# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrosekLE',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('delilnik_vrednost', models.DecimalField(max_digits=8, decimal_places=4)),
                ('lastniska_enota', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna')),
                ('strosek', models.ForeignKey(to='racunovodstvo.Strosek')),
            ],
            options={
                'verbose_name_plural': 'stroški na LE',
                'verbose_name': 'strošek na LE',
            },
        ),
    ]
