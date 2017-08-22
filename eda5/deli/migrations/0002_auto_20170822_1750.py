# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('etaznalastnina', '__first__'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projektnomesto',
            name='tip_elementa',
            field=models.ForeignKey(to='katalog.TipArtikla', verbose_name='Tip Elementa', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
        migrations.AddField(
            model_name='nastavitev',
            name='element',
            field=models.ForeignKey(to='deli.Element'),
        ),
        migrations.AddField(
            model_name='nastavitev',
            name='obratovalni_parameter',
            field=models.ForeignKey(to='katalog.ObratovalniParameter'),
        ),
        migrations.AddField(
            model_name='lokacija',
            name='etaza',
            field=models.ForeignKey(to='deli.Etaza', verbose_name='Etaža'),
        ),
        migrations.AddField(
            model_name='lokacija',
            name='prostor',
            field=models.OneToOneField(to='deli.DelStavbe', verbose_name='Prostor'),
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(to='deli.Stavba', verbose_name='Stavba'),
        ),
        migrations.AddField(
            model_name='element',
            name='artikel',
            field=models.ForeignKey(to='katalog.ModelArtikla', verbose_name='Model', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='projektno_mesto',
            field=models.ForeignKey(to='deli.ProjektnoMesto', verbose_name='projektno mesto'),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='lastniska_skupina',
            field=models.ForeignKey(to='etaznalastnina.LastniskaSkupina', verbose_name='lastniška skupina', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='podskupina',
            field=models.ForeignKey(to='deli.Podskupina'),
        ),
    ]
