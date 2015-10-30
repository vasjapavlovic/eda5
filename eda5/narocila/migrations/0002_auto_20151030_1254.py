# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narocilo',
            name='narocilo_pogodba',
            field=models.OneToOneField(blank=True, null=True, to='narocila.NarociloPogodba'),
        ),
        migrations.AlterField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(blank=True, null=True, to='narocila.NarociloTelefon'),
        ),
    ]
