# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('narocila', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('delovninalogi', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('deli', '0002_auto_20151215_1854'),
        ('posta', '0001_initial'),
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
            field=models.ForeignKey(to='katalog.ModelArtikla', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.ForeignKey(to='delovninalogi.DelovniNalog', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='delstavbe',
            field=models.ForeignKey(to='deli.DelStavbe', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='dokument',
            field=models.OneToOneField(to='posta.Dokument', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='element',
            field=models.ForeignKey(to='deli.Element', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(to='arhiv.ArhivMesto', blank=True, null=True, verbose_name='lokacija hrambe'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='narocilo',
            field=models.ForeignKey(to='narocila.Narocilo', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', blank=True, null=True),
        ),
    ]
