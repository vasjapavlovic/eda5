# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0002_lastniskaenotaelaborat_posta'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='lastniski_delez',
            field=models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=4, verbose_name='lastniški delež'),
        ),
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='program',
            field=models.ForeignKey(blank=True, null=True, to='etaznalastnina.Program'),
        ),
    ]
