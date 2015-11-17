# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20151117_1404'),
        ('katalog', '0002_remove_modelartikla_prejeta_dokumentacija'),
        ('narocila', '0002_auto_20151117_1404'),
        ('posta', '0014_auto_20151117_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='artikel',
            field=models.ForeignKey(null=True, to='katalog.ModelArtikla', blank=True),
        ),
        migrations.AddField(
            model_name='dokument',
            name='delstavbe',
            field=models.ForeignKey(null=True, to='deli.DelStavbe', blank=True),
        ),
        migrations.AddField(
            model_name='dokument',
            name='element',
            field=models.ForeignKey(null=True, to='deli.Element', blank=True),
        ),
        migrations.AddField(
            model_name='dokument',
            name='narocilo',
            field=models.ForeignKey(null=True, to='narocila.Narocilo', blank=True),
        ),
    ]
