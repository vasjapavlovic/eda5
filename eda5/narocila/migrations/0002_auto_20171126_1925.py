# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '__first__'),
        ('partnerji', '__first__'),
        ('zahtevki', '__first__'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilo',
            name='izvajalec',
            field=models.ForeignKey(to='partnerji.Partner', related_name='izvajalec', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(null=True, to='narocila.NarociloTelefon', blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(to='partnerji.Partner', related_name='narocnik', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='narocilo',
            name='zahtevek',
            field=models.ForeignKey(null=True, to='zahtevki.Zahtevek', blank=True),
        ),
        migrations.AddField(
            model_name='narocilodokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(to='posta.VrstaDokumenta', verbose_name='vrsta dokumenta', default=1),
            preserve_default=False,
        ),
    ]
