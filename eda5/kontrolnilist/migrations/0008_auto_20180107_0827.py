# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0007_auto_20180107_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='vrednost_check',
            field=models.BooleanField(verbose_name='vrednost check', default=False),
        ),
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='vrednost_select',
            field=models.ForeignKey(null=True, blank=True, to='kontrolnilist.KontrolaSpecifikacijaOpcijaSelect', verbose_name='vrednost select'),
        ),
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='vrednost_text',
            field=models.CharField(blank=True, null=True, verbose_name='vrednost tekst', max_length=255),
        ),
    ]
