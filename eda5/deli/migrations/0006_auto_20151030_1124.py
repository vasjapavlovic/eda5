# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151026_0727'),
        ('deli', '0005_auto_20151030_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='delstavbe',
            name='prejeta_dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
        migrations.AddField(
            model_name='element',
            name='dokumentacija',
            field=models.FileField(upload_to=eda5.deli.models.Element.dokumentacija_directory_path, blank=True, verbose_name='shema sistema'),
        ),
        migrations.AddField(
            model_name='element',
            name='prejeta_dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
    ]
