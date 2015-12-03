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
            field=models.ForeignKey(to='partnerji.Partner', related_name='izvajalec'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_pogodba',
            field=models.OneToOneField(to='narocila.NarociloPogodba', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(to='narocila.NarociloTelefon', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='narocnik'),
        ),
    ]
