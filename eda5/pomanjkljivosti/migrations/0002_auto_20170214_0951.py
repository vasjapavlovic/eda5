# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='lokacija',
            new_name='element_text',
        ),
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='etaza',
            new_name='etaza_text',
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='lokacija_text',
            field=models.CharField(default='nedefinirano', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='element',
            field=models.ForeignKey(null=True, to='deli.ProjektnoMesto', blank=True),
        ),
    ]
