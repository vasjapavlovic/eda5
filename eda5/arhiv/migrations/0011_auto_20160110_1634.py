# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0010_arhiviranje_zahtevek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.ForeignKey(blank=True, to='delovninalogi.DelovniNalog', null=True),
        ),
    ]
