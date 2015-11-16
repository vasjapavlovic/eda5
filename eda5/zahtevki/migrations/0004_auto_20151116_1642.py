# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0003_auto_20151115_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='datum_nastanka_skode',
            field=models.DateField(blank=True, null=True, verbose_name='datum nastanka škode'),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='povzrocitelj',
            field=models.CharField(max_length=255, blank=True, verbose_name='povzročitelj (opisno)'),
        ),
    ]
