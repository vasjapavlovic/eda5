# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0007_auto_20151030_1131'),
        ('posta', '0008_auto_20151026_0727'),
        ('partnerji', '0013_auto_20151030_1310'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum', models.DateField()),
                ('sklicatelj', models.ForeignKey(to='partnerji.Partner')),
                ('zapisnik', models.ForeignKey(to='posta.Dokument', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'sestanki',
                'ordering': ('datum',),
                'verbose_name': 'sestanek',
            },
        ),
        migrations.AlterModelOptions(
            name='zahtevekskodnidogodek',
            options={'ordering': ('datum_nastanka_skode',), 'verbose_name': 'škodni dogodek', 'verbose_name_plural': 'škodni dogodki'},
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')]),
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='datum_nastanka_skode',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='datum nastanka škdoe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='dokazno_gradivo',
            field=models.ForeignKey(to='posta.Dokument', related_name='dokazno_gradivo', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='is_prijava_policiji',
            field=models.BooleanField(default=False, verbose_name='prijavljeno policiji'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='poskodovane_stvari',
            field=models.ManyToManyField(to='deli.Element', blank=True),
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='povzrocitelj',
            field=models.CharField(max_length=255, blank=True, verbose_name='povzročitelj'),
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='predvidena_skoda',
            field=models.DecimalField(default=100, max_digits=7, decimal_places=2, blank=True, verbose_name='predvidena škoda'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='vzrok_skode',
            field=models.TextField(blank=True, verbose_name='vzrok škode'),
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
            field=models.OneToOneField(to='zahtevki.ZahtevekSkodniDogodek', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='dokument_poravnava',
            field=models.ForeignKey(to='posta.Dokument', related_name='dokument_poravnava', blank=True, verbose_name='poravnava škode', null=True),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='dokument_prijava_skode',
            field=models.ForeignKey(to='posta.Dokument', related_name='dokument_prijava_skode', blank=True, verbose_name='prijava škode', null=True),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='dokument_zapisnik_ogleda',
            field=models.ForeignKey(to='posta.Dokument', related_name='dokument_zapisnik_ogleda', blank=True, verbose_name='zapisnik o ogledu škode', null=True),
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_sestanek',
            field=models.OneToOneField(to='zahtevki.ZahtevekSestanek', blank=True, null=True),
        ),
    ]
