# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0003_auto_20160117_1956'),
        ('arhiv', '0011_auto_20160110_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arhiviranje',
            name='narocilo',
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='narocilo_dokument',
            field=models.ForeignKey(blank=True, null=True, to='narocila.NarociloDokument'),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='artikel',
            field=models.ForeignKey(blank=True, null=True, to='katalog.ModelArtikla'),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.ForeignKey(blank=True, null=True, to='deli.DelStavbe'),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='element',
            field=models.ForeignKey(blank=True, null=True, to='deli.Element'),
        ),
    ]
