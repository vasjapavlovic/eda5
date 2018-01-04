# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogodek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('datum_dogodka', models.DateField(verbose_name='datum dogodka')),
                ('opis_dogodka', models.TextField(verbose_name='opis dogodka')),
                ('is_potrebna_prijava_policiji', models.NullBooleanField(verbose_name='potrebna prijava policiji?')),
                ('is_nastala_skoda', models.NullBooleanField(verbose_name='Je nastala škoda?')),
                ('povzrocitelj', models.CharField(verbose_name='povzročitelj (opisno)', max_length=255, blank=True)),
                ('cas_dogodka', models.TimeField(verbose_name='okvirni čas dogodka', null=True, blank=True)),
                ('predvidena_visina_skode', models.DecimalField(verbose_name='predvidena višina škode', decimal_places=2, null=True, blank=True, max_digits=7)),
                ('poravnava_skode', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='poravnava_skode')),
                ('prijava_policiji', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='prijava_policiji')),
                ('prijava_skode', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='prijava_skode')),
                ('racun_za_popravilo', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='racun_za_popravilo')),
            ],
            options={
                'verbose_name': 'dogodek',
                'verbose_name_plural': 'dogodki',
            },
        ),
    ]
