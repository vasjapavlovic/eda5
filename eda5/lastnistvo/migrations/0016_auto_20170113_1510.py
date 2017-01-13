# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0015_auto_20170112_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='najemlastnine',
            name='is_active',
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='opombe',
            field=models.OneToOneField(to='lastnistvo.NajemLastnine', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='opombe',
            field=models.OneToOneField(to='lastnistvo.ProdajaLastnine', null=True, blank=True),
        ),
    ]
