# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0005_auto_20151116_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arhiviranje',
            name='arhiviral',
        ),
        migrations.RemoveField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
        ),
        migrations.RemoveField(
            model_name='arhivmesto',
            name='arhiv',
        ),
        migrations.AlterField(
            model_name='dokument',
            name='arhiviranje',
            field=models.OneToOneField(to='arhiv.Arhiviranje', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Arhiv',
        ),
        migrations.DeleteModel(
            name='Arhiviranje',
        ),
        migrations.DeleteModel(
            name='ArhivMesto',
        ),
    ]
