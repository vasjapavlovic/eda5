# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilo',
            name='izvajalec',
            field=models.ForeignKey(related_name='izvajalec', to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_pogodba',
            field=models.OneToOneField(null=True, to='narocila.NarociloPogodba', blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(null=True, to='narocila.NarociloTelefon', blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(related_name='narocnik', to='partnerji.SkupinaPartnerjev'),
        ),
    ]
