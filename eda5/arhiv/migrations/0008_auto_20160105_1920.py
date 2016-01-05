# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0004_auto_20160102_1407'),
        ('delovninalogi', '0005_vzorecopravila'),
        ('arhiv', '0007_auto_20160104_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhivmesto',
            name='delovni_nalog',
            field=models.OneToOneField(null=True, to='delovninalogi.DelovniNalog', blank=True),
        ),
        migrations.AddField(
            model_name='arhivmesto',
            name='zahtevek',
            field=models.OneToOneField(null=True, to='zahtevki.Zahtevek', blank=True),
        ),
    ]
