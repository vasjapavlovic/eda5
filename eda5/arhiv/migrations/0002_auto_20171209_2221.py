# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('povprasevanje', '__first__'),
        ('dogodki', '__first__'),
        ('deli', '0001_initial'),
        ('posta', '__first__'),
        ('skladisce', '__first__'),
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.ForeignKey(null=True, blank=True, to='deli.DelStavbe'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='dobava',
            field=models.ForeignKey(null=True, blank=True, to='skladisce.Dobava'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='dogodek',
            field=models.ForeignKey(null=True, blank=True, to='dogodki.Dogodek'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='dokument',
            field=models.OneToOneField(null=True, to='posta.Dokument', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='element',
            field=models.ForeignKey(null=True, blank=True, to='deli.Element'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(null=True, verbose_name='lokacija hrambe', blank=True, to='arhiv.ArhivMesto'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='povprasevanje',
            field=models.ForeignKey(null=True, blank=True, to='povprasevanje.Povprasevanje'),
        ),
    ]
