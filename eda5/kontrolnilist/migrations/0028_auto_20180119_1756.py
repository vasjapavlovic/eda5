# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0027_remove_kontrolaspecifikacija_aktivnost'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='perioda_enota',
            field=models.CharField(max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], verbose_name='Perioda ENOTA', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='perioda_enota_kolicina',
            field=models.IntegerField(verbose_name='Perioda KRATNIK ENOTE', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='perioda_kolicina_na_enoto',
            field=models.IntegerField(verbose_name='Perioda KOLIČINA NA ENOTO', default=1),
            preserve_default=False,
        ),
    ]
