# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0003_racun_stavba'),
        ('razdelilnik', '0005_razdelilnik_zahtevek'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrosekRazdelilnik',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('is_razdeljen', models.BooleanField(default=False)),
                ('razdeljen_datum', models.DateField(null=True, blank=True)),
                ('razdelilnik', models.ForeignKey(to='razdelilnik.Razdelilnik')),
                ('strosek', models.OneToOneField(to='racunovodstvo.Strosek')),
            ],
            options={
                'verbose_name_plural': 'StrosekRazdelilnik',
                'verbose_name': 'StrosekRazdelilnik',
            },
        ),
    ]
