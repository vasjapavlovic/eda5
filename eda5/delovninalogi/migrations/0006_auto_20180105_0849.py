# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0005_auto_20180104_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aktivnost',
            options={'verbose_name_plural': 'Aktivnosti', 'verbose_name': 'Aktivnost', 'ordering': ('oznaka',)},
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='opravilo',
            field=models.ForeignKey(to='delovninalogi.Opravilo', null=True, verbose_name='opravilo', blank=True),
        ),
    ]
