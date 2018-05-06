# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0001_initial'),
        ('racunovodstvo', '0002_vrstastroska_opis'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosek',
            name='narocilo',
            field=models.ForeignKey(to='narocila.Narocilo', verbose_name='ID Naročila', null=True, blank=True),
        ),
    ]
