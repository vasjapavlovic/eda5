# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0006_auto_20160104_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiviranje',
            name='artikel',
            field=models.OneToOneField(blank=True, to='katalog.ModelArtikla', null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.OneToOneField(blank=True, to='delovninalogi.DelovniNalog', null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.OneToOneField(blank=True, to='deli.DelStavbe', null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='element',
            field=models.OneToOneField(blank=True, to='deli.Element', null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='narocilo',
            field=models.OneToOneField(blank=True, to='narocila.Narocilo', null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.OneToOneField(blank=True, to='zahtevki.Zahtevek', null=True),
        ),
    ]
