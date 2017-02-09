# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0015_auto_20170209_1601'),
        ('narocila', '0006_auto_20170208_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='narocilo',
            name='narocilo_dokument',
        ),
        migrations.AddField(
            model_name='narocilodokument',
            name='dokument',
            field=models.ForeignKey(to='arhiv.Arhiviranje', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='narocilodokument',
            name='narocilo',
            field=models.OneToOneField(to='narocila.Narocilo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='narocilo',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
