# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0013_arhiviranje_dogodek'),
        ('lastnistvo', '0013_auto_20160102_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='najemlastnine',
            old_name='datum_predaje',
            new_name='predaja_datum',
        ),
        migrations.RenameField(
            model_name='najemlastnine',
            old_name='datum_veljavnosti',
            new_name='veljavnost_datum',
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='najemna_pogodba',
            field=models.ForeignKey(null=True, blank=True, related_name='najemna_pogodba', to='arhiv.Arhiviranje'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='veljavnost_trajanje_opisno',
            field=models.CharField(null=True, max_length=255, blank=True, verbose_name='trajanje pogodbe'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='vracilo_datum',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='vracilo_posebnosti',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='vracilo_zapisnik',
            field=models.ForeignKey(null=True, blank=True, related_name='izrocitev_lastnine', to='arhiv.Arhiviranje'),
        ),
    ]
