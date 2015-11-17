# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_skupinapartnerjev_oznaka'),
        ('posta', '0012_auto_20151117_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='likvidiral',
            field=models.ForeignKey(default=1, verbose_name='pošto bo likvidiral', to='partnerji.Oseba', related_name='likvidiral'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aktivnost',
            name='izvajalec',
            field=models.ForeignKey(to='partnerji.Oseba', verbose_name='izvajalec poštne storitve', related_name='izvajalec'),
        ),
    ]
