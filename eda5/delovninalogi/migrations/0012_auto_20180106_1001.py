# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0011_auto_20180105_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='opravilo',
        ),
        migrations.RemoveField(
            model_name='aktivnost',
            name='projektno_mesto',
        ),
        migrations.RemoveField(
            model_name='aktivnostparameterspecifikacija',
            name='aktivnost',
        ),
        migrations.RemoveField(
            model_name='opcijaselect',
            name='aktivnost_parameter_specifikacija',
        ),
        migrations.DeleteModel(
            name='Aktivnost',
        ),
        migrations.DeleteModel(
            name='AktivnostParameterSpecifikacija',
        ),
        migrations.DeleteModel(
            name='OpcijaSelect',
        ),
    ]
