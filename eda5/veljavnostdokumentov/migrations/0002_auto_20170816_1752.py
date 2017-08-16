# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0008_auto_20170814_1611'),
        ('deli', '__first__'),
        ('veljavnostdokumentov', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veljavnostdokumenta',
            name='stavba',
            field=models.ForeignKey(verbose_name='stavba', to='deli.Stavba', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='veljavnostdokumenta',
            name='vrsta_stroska',
            field=models.ForeignKey(verbose_name='Vrsta Stroška', to='racunovodstvo.VrstaStroska', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='veljavnostdokumenta',
            name='velja_od',
            field=models.DateField(null=True, verbose_name='velja od', blank=True),
        ),
    ]
