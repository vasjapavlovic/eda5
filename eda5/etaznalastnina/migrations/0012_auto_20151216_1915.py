# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0011_remove_inernadodatno_uporabno_dovoljenje'),
    ]

    operations = [
        migrations.CreateModel(
            name='UporabnoDovoljenje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('st_dokumenta', models.CharField(max_length=50, unique=True)),
                ('datum', models.DateField()),
                ('objekt', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'uporabna dovoljenja',
                'verbose_name': 'uporabno dovoljenje',
            },
        ),
        migrations.AddField(
            model_name='inernadodatno',
            name='uporabno_dovoljenje',
            field=models.ForeignKey(to='etaznalastnina.UporabnoDovoljenje', null=True, blank=True),
        ),
    ]
