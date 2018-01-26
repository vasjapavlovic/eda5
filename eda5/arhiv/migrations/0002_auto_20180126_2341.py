# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
        ('reklamacije', '0001_initial'),
        ('deli', '0001_initial'),
        ('dogodki', '0001_initial'),
        ('povprasevanje', '0001_initial'),
        ('posta', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('razdelilnik', '0001_initial'),
        ('sestanki', '0001_initial'),
        ('skladisce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='delovninalog',
            field=models.ForeignKey(null=True, blank=True, to='delovninalogi.DelovniNalog'),
        ),
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
            field=models.OneToOneField(null=True, blank=True, to='posta.Dokument'),
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
        migrations.AddField(
            model_name='arhiviranje',
            name='racun',
            field=models.OneToOneField(null=True, blank=True, to='racunovodstvo.Racun'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='razdelilnik',
            field=models.ForeignKey(null=True, blank=True, to='razdelilnik.Razdelilnik'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='reklamacija',
            field=models.ForeignKey(null=True, blank=True, to='reklamacije.Reklamacija'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='sestanek',
            field=models.ForeignKey(null=True, blank=True, to='sestanki.Sestanek'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
