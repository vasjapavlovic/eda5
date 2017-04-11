# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0002_opombasklepa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opombasklepa',
            name='sklep',
            field=models.ForeignKey(verbose_name='sklep sestanka', to='sestanki.Sklep'),
        ),
    ]
