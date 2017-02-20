# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0007_auto_20170209_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='narocilotelefon',
            options={'verbose_name_plural': 'naročila po telefonu', 'verbose_name': 'ustno/telefonsko naročilo'},
        ),
        migrations.RemoveField(
            model_name='narocilotelefon',
            name='cas_klica',
        ),
        migrations.RemoveField(
            model_name='narocilotelefon',
            name='datum_klica',
        ),
        migrations.RemoveField(
            model_name='narocilotelefon',
            name='oseba',
        ),
        migrations.RemoveField(
            model_name='narocilotelefon',
            name='telefonska_stevilka',
        ),
        migrations.RemoveField(
            model_name='narocilotelefon',
            name='telefonsko_sporocilo',
        ),
        migrations.AddField(
            model_name='narocilotelefon',
            name='dogovor_date',
            field=models.DateField(default=datetime.datetime.now().date(), verbose_name='datum dogovora'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='narocilotelefon',
            name='dogovor_person',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Oseba s katero si se dogovarjal'),
        ),
        migrations.AddField(
            model_name='narocilotelefon',
            name='dogovor_phonenumber',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='telefonska številka'),
        ),
        migrations.AddField(
            model_name='narocilotelefon',
            name='dogovor_text',
            field=models.CharField(default='NA', max_length=255, verbose_name='opis dogovora'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='narocilotelefon',
            name='dogovor_time',
            field=models.TimeField(default=datetime.datetime.now().time(), verbose_name='čas dogovora'),
            preserve_default=False,
        ),
    ]
