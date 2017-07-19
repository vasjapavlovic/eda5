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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('delilnik_vrednost', models.DecimalField(decimal_places=4, max_digits=8)),
                ('lastniska_enota', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna')),
                ('strosek', models.ForeignKey(to='racunovodstvo.Strosek')),
            ],
            options={
                'verbose_name_plural': 'stroški na LE',
                'verbose_name': 'strošek na LE',
            },
        ),
    ]
