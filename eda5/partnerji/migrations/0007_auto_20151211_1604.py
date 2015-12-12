# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0006_auto_20151211_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skupinapartnerjev',
            old_name='davcna_st',
            new_name='oznaka',
        ),
    ]
