# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0007_partner_davcni_zavezanec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banka',
            name='naslov',
        ),
        migrations.RemoveField(
            model_name='banka',
            name='naziv',
        ),
        migrations.RemoveField(
            model_name='banka',
            name='posta',
        ),
        migrations.AddField(
            model_name='banka',
            name='partner',
            field=models.OneToOneField(to='partnerji.Partner', blank=True, default=1),
            preserve_default=False,
        ),
    ]
