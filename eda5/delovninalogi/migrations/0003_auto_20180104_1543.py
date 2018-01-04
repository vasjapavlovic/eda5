# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0001_initial'),
        ('deli', '0002_auto_20180104_1543'),
        ('delovninalogi', '0002_vzorecopravila_narocilo'),
        ('naloge', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('narocila', '0002_auto_20180104_1543'),
        ('planiranje', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vzorecopravila',
            name='nosilec',
            field=models.ForeignKey(to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='vzorecopravila',
            name='planirano_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo'),
        ),
        migrations.AddField(
            model_name='vzorecopravila',
            name='vrsta_stroska',
            field=models.ForeignKey(null=True, blank=True, verbose_name='vrsta stroška', to='racunovodstvo.VrstaStroska'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='naloga',
            field=models.ManyToManyField(to='naloge.Naloga', blank=True),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='narocilo',
            field=models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='nosilec',
            field=models.ForeignKey(to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='planirano_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='pomanjkljivost',
            field=models.ManyToManyField(to='pomanjkljivosti.Pomanjkljivost', blank=True),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='vrsta_stroska',
            field=models.ForeignKey(null=True, blank=True, verbose_name='vrsta stroška', to='racunovodstvo.VrstaStroska'),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek'),
        ),
        migrations.AddField(
            model_name='delovrsta',
            name='skupina',
            field=models.ForeignKey(to='delovninalogi.DeloVrstaSklop'),
        ),
        migrations.AddField(
            model_name='delovninalog',
            name='nosilec',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Izvajalec (kdo bo delo izvedel)', to='partnerji.Oseba'),
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
            field=models.ForeignKey(null=True, blank=True, to='delovninalogi.DeloVrsta'),
        ),
    ]
