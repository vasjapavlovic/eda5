# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0010_obratovalniparameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='obratovalniparameter',
            name='artikel',
            field=models.ForeignKey(to='katalog.ModelArtikla', blank=True, null=True),
        ),
    ]
