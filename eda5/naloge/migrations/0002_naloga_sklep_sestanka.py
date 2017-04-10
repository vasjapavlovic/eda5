# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '__first__'),
        ('naloge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='naloga',
            name='sklep_sestanka',
            field=models.ForeignKey(null=True, to='sestanki.Sklep', blank=True, verbose_name='sklep sestanka'),
        ),
    ]
