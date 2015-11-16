# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0009_remove_dokument_arhiviranje'),
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='dokument',
            field=models.OneToOneField(to='posta.Dokument', default=10),
            preserve_default=False,
        ),
    ]
