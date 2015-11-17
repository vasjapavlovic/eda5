# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20151117_1404'),
        ('katalog', '0002_remove_modelartikla_prejeta_dokumentacija'),
        ('delovninalogi', '0003_remove_delovninalog_dokument'),
        ('zahtevki', '0007_auto_20151117_1404'),
        ('narocila', '0002_auto_20151117_1404'),
        ('arhiv', '0005_remove_arhivmesto_zahtevek'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='artikel',
            field=models.ForeignKey(blank=True, null=True, to='katalog.ModelArtikla'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.ForeignKey(blank=True, null=True, to='delovninalogi.DelovniNalog'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.ForeignKey(blank=True, null=True, to='deli.DelStavbe'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='element',
            field=models.ForeignKey(blank=True, null=True, to='deli.Element'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='narocilo',
            field=models.ForeignKey(blank=True, null=True, to='narocila.Narocilo'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(blank=True, null=True, to='zahtevki.Zahtevek'),
        ),
    ]
