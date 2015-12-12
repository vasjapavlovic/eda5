# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20151203_0301'),
        ('racunovodstvo', '0004_auto_20151211_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='narocilo',
            field=models.ForeignKey(blank=True, to='narocila.Narocilo', null=True),
        ),
        migrations.AlterField(
            model_name='racun',
            name='davcna_klasifikacija',
            field=models.IntegerField(choices=[(0, 'podjetje'), (1, 'razdelilnik')]),
        ),
        migrations.DeleteModel(
            name='DavcnaKlasifikacija',
        ),
    ]
