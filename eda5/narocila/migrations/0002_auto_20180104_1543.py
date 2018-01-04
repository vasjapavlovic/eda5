# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0001_initial'),
        ('posta', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilodokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='izvajalec',
            field=models.ForeignKey(to='partnerji.Partner', related_name='izvajalec'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(null=True, blank=True, to='narocila.NarociloTelefon'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(to='partnerji.Partner', related_name='narocnik'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
