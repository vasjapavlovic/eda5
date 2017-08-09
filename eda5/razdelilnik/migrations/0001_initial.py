# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '__first__'),
        ('racunovodstvo', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrosekLE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
