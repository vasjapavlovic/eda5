# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0014_remove_arhiviranje_dogodek'),
        ('veljavnostdokumentov', '0002_auto_20170205_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veljavnostdokumenta',
            name='dokument',
        ),
        migrations.AddField(
            model_name='veljavnostdokumenta',
            name='arhiviranje',
            field=models.OneToOneField(to='arhiv.Arhiviranje', verbose_name='arhiviranje', default=1),
            preserve_default=False,
        ),
    ]
