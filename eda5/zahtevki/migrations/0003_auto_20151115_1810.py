# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0002_auto_20151112_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahtevek',
            name='zahtevek_izvedba_dela',
        ),
        migrations.RemoveField(
            model_name='zahtevek',
            name='zahtevek_sestanek',
        ),
        migrations.RemoveField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='vrsta',
            field=models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahtevekizvedbadela',
            name='zahtevek',
            field=models.OneToOneField(to='zahtevki.Zahtevek', default=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahteveksestanek',
            name='zahtevek',
            field=models.OneToOneField(to='zahtevki.Zahtevek', default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='zahtevek',
            field=models.OneToOneField(to='zahtevki.Zahtevek', default=22),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zahtevekizvedbadela',
            name='is_zakonska_obveza',
            field=models.NullBooleanField(verbose_name='zakonska obveza'),
        ),
        migrations.AlterField(
            model_name='zahteveksestanek',
            name='datum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zahteveksestanek',
            name='sklicatelj',
            field=models.ForeignKey(to='partnerji.Partner', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zahteveksestanek',
            name='udelezenci',
            field=models.ManyToManyField(to='partnerji.Oseba', blank=True, verbose_name='udeleženci'),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='datum_nastanka_skode',
            field=models.DateField(verbose_name='datum nastanka škdoe', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='is_prijava_policiji',
            field=models.NullBooleanField(verbose_name='prijavljeno policiji'),
        ),
    ]