# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogodek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('datum_dogodka', models.DateField(verbose_name='datum dogodka')),
                ('opis_dogodka', models.TextField(verbose_name='opis dogodka')),
                ('is_potrebna_prijava_policiji', models.NullBooleanField(verbose_name='potrebna prijava policiji?')),
                ('is_nastala_skoda', models.NullBooleanField(verbose_name='Je nastala škoda?')),
                ('povzrocitelj', models.CharField(blank=True, max_length=255, verbose_name='povzročitelj (opisno)')),
                ('cas_dogodka', models.TimeField(blank=True, null=True, verbose_name='okvirni čas dogodka')),
                ('predvidena_visina_skode', models.DecimalField(blank=True, max_digits=7, decimal_places=2, null=True, verbose_name='predvidena višina škode')),
                ('poravnava_skode', models.ForeignKey(related_name='poravnava_skode', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('prijava_policiji', models.ForeignKey(related_name='prijava_policiji', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('prijava_skode', models.ForeignKey(related_name='prijava_skode', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('racun_za_popravilo', models.ForeignKey(related_name='racun_za_popravilo', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'dogodki',
                'verbose_name': 'dogodek',
            },
        ),
    ]
