# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etaznalastninaelaborat',
            options={'verbose_name': 'etažna lastnina elaborat', 'ordering': ('oznaka',), 'verbose_name_plural': 'etažna lastnina elaborat'},
        ),
        migrations.AlterModelOptions(
            name='etaznalastninainterna',
            options={'verbose_name': 'etažna lastnina interna', 'ordering': ('oznaka',), 'verbose_name_plural': 'etažna lastnina interna'},
        ),
        migrations.AlterField(
            model_name='etaznalastninainterna',
            name='oznaka',
            field=models.CharField(verbose_name='interna številka dela stavbe', max_length=5),
        ),
    ]
