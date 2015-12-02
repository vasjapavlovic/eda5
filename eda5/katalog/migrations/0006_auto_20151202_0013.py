# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_remove_planov_oznaka'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikelPlan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('naziv', models.CharField(max_length=255)),
                ('perioda_predpisana_enota', models.CharField(max_length=5, verbose_name='enota periode', choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('element', models.ForeignKey(to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name_plural': 'Plan Obratovanja in Vzdrževanja',
                'verbose_name': 'Plan Obratovanja in Vzdrževanja',
            },
        ),
        migrations.RemoveField(
            model_name='planov',
            name='element',
        ),
        migrations.RemoveField(
            model_name='planov',
            name='plan_opravilo',
        ),
        migrations.DeleteModel(
            name='PlanOV',
        ),
    ]
