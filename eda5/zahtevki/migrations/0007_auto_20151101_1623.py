# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0006_auto_20151101_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_zakonska_obveza', models.BooleanField(verbose_name='zakonska obveza')),
            ],
            options={
                'verbose_name': 'izvedba dela',
                'verbose_name_plural': 'izvedba del',
            },
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_izvedba_dela',
            field=models.OneToOneField(to='zahtevki.ZahtevekIzvedbaDela', blank=True, null=True),
        ),
    ]
