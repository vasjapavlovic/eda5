# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('delovninalogi', '0001_initial'),
        ('narocila', '0001_initial'),
        ('posta', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('katalog', '0001_initial'),
        ('deli', '0002_auto_20151122_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='arhiviral',
            field=models.ForeignKey(to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='artikel',
            field=models.ForeignKey(null=True, to='katalog.ModelArtikla', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.ForeignKey(null=True, to='delovninalogi.DelovniNalog', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.ForeignKey(null=True, to='deli.DelStavbe', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='dokument',
            field=models.OneToOneField(null=True, to='posta.Dokument', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='element',
            field=models.ForeignKey(null=True, to='deli.Element', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(null=True, verbose_name='lokacija hrambe', to='arhiv.ArhivMesto', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='narocilo',
            field=models.ForeignKey(null=True, to='narocila.Narocilo', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(null=True, to='zahtevki.Zahtevek', blank=True),
        ),
    ]
