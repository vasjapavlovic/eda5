# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '__first__'),
        ('veljavnostdokumentov', '0003_veljavnostdokumenta_planirano_opravilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veljavnostdokumenta',
            name='narocilo',
            field=models.ForeignKey(to='narocila.Narocilo', blank=True, verbose_name='Narocilo', null=True),
        ),
    ]
