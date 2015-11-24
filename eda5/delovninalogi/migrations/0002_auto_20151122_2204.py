# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('delovninalogi', '0001_initial'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='nadzornik',
            field=models.ForeignKey(to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='narocilo',
            field=models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek'),
        ),
        migrations.AddField(
            model_name='delovrsta',
            name='sklo',
            field=models.ForeignKey(to='delovninalogi.DeloVrstaSklop'),
        ),
        migrations.AddField(
            model_name='delovninalog',
            name='nosilec',
            field=models.ForeignKey(null=True, to='partnerji.Oseba', blank=True),
        ),
        migrations.AddField(
            model_name='delovninalog',
            name='opravilo',
            field=models.ForeignKey(to='delovninalogi.Opravilo'),
        ),
        migrations.AddField(
            model_name='delo',
            name='delavec',
            field=models.ForeignKey(to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='delo',
            name='delovninalog',
            field=models.ForeignKey(verbose_name='delovni nalog', to='delovninalogi.DelovniNalog'),
        ),
        migrations.AddField(
            model_name='delo',
            name='vrsta_dela',
            field=models.ForeignKey(null=True, to='delovninalogi.DeloVrsta', blank=True),
        ),
    ]
